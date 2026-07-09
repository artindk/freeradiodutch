# -*- coding: utf-8 -*-
# FreeRadio - Time-shift buffer
#
# Captures the currently playing live stream into a local rolling buffer
# file so the user can rewind and re-listen to the last few minutes, like a
# cassette tape / DVR. Capture runs over an independent HTTP/ICY connection,
# completely separate from the BASS playback engine used for normal live
# listening - it never touches bass_host.py's audio pipeline.
#
# Design notes (see the design document for the full rationale):
#   - Plain HTTP(S) streams AND HLS (.m3u8) streams are both supported, and
#     both write into the exact same rolling buffer file mechanism below
#     (_write_chunk / _maybe_trim / generation counter / suspend-trim).
#     Only how bytes are *acquired* differs:
#       * Plain HTTP/ICY: raw bytes are read straight off the socket (_run).
#       * HLS: the master playlist is resolved to the best media playlist,
#         then new segments are downloaded in order over plain HTTP and
#         their raw bytes are appended to the buffer exactly like a plain
#         stream would be (_run_hls). This mirrors what recorder.py already
#         does for HLS recordings - concatenating segment bytes into a
#         single playable file - so the same BASS_StreamCreateFile() call
#         used for the plain-HTTP buffer in bass_host.py also works
#         unchanged for the HLS buffer; no separate HLS playback path is
#         needed.
#   - The buffer stores the raw encoded bytes exactly as received (MP3/AAC/
#     OGG/MPEG-TS/fMP4/etc.), matching what recorder.py already does for
#     recordings.
#   - fMP4-packaged HLS streams carry required initialization data (a moov
#     box) in a separate #EXT-X-MAP segment. That segment is written once,
#     at the very start of the buffer file, and its length is recorded in
#     _reserved_prefix_len so _maybe_trim() can never trim it away -
#     trimming into it would make the whole buffer file undecodable.
#     _reserved_prefix_len is 0 for plain HTTP and TS-packaged HLS streams,
#     so trimming behaves exactly as before for those.
#   - The buffer is trimmed to CAPACITY_SECONDS only while nothing is
#     currently reading it for time-shifted playback (see enter_playback/
#     exit_playback). This avoids rewriting a file out from under an
#     actively open BASS file stream. While a time-shift session is active,
#     the buffer may temporarily grow past the configured capacity; trimming
#     resumes as soon as the user returns to live.
#   - Trim uses an average bytes-per-second estimate for the session. This
#     is approximate for variable-bitrate streams but adequate for a rolling
#     "last N minutes" window. Trim only ever drops bytes that come after
#     _reserved_prefix_len, so a preserved fMP4 init segment (see above) is
#     never touched.
#   - Generation counter: every start() call bumps a generation number, and
#     the capture thread checks it belongs to the current generation before
#     every write and on every loop iteration. This guarantees a stale
#     thread from a previous station can never keep writing into (or being
#     read back from) the buffer, even if stop() was skipped or delayed for
#     any reason - the thread notices on its own and exits.
#   - The buffer file is kept open for the whole capture session instead of
#     being reopened for every chunk, to minimize disk I/O overhead (many
#     open/close syscalls per second can contribute to audio stutter on the
#     live stream, since capture competes for system resources).

import logging
import os
import tempfile
import threading
import time
import urllib.request

from . import recorder as _recorder_mod

log = logging.getLogger()

_CHUNK = 65536


class TimeShiftBuffer:
	"""Continuously captures the currently playing stream to a local file
	so it can be rewound and replayed. Only one capture session is active
	at a time, matching the single "now playing" station of the main
	player.
	"""

	CAPACITY_SECONDS = 600          # 10 minutes
	_TRIM_MARGIN_SECONDS = 120       # trim only once ~2 minutes over capacity
	_TRIM_CHECK_INTERVAL = 30        # seconds between trim checks

	def __init__(self, tmp_dir=None):
		self._tmp_dir = tmp_dir or tempfile.gettempdir()
		self._thread = None
		self._stop_event = threading.Event()
		self._file_path = None
		self._file_lock = threading.Lock()   # guards the persistent file handle
		self._file_handle = None             # persistent handle, opened for the whole session
		self._session_start = None
		self._bytes_written = 0
		self._active = False
		self._suspend_trim = False   # True while a time-shift playback session has the file open
		self._url = None
		self._is_hls = False         # True if the current session is capturing via HLS segments
		self._hls_skipped = False    # True only if the HLS manifest itself could not be read at all
		self._reserved_prefix_len = 0  # bytes at the head of the buffer that _maybe_trim must never drop
		self._generation = 0         # bumped on every start(); stale threads self-terminate

	# -- Public API ---------------------------------------------------------

	def start(self, url):
		"""Begin capturing *url* into a fresh buffer file. Any previous
		session is stopped and its temp file removed first.

		Both plain HTTP(S) streams and HLS (.m3u8) streams are captured
		into the same kind of rolling buffer file - see the module design
		notes above. is_hls_skipped() only reports True if the HLS
		manifest itself could not be read at all (see _run_hls).
		"""
		self.stop()

		self._generation += 1
		my_gen = self._generation

		self._stop_event = threading.Event()
		self._url = url
		self._is_hls = url.lower().split("?")[0].endswith(".m3u8")
		self._hls_skipped = False
		self._session_start = time.time()
		self._bytes_written = 0
		self._suspend_trim = False
		self._reserved_prefix_len = 0

		try:
			fd, path = tempfile.mkstemp(prefix="freeradio_timeshift_", suffix=".buf", dir=self._tmp_dir)
			os.close(fd)
		except OSError as e:
			log.warning("FreeRadio TimeShift: could not create buffer file: %s", e)
			return

		self._file_path = path
		self._active = True
		target = self._run_hls if self._is_hls else self._run
		thread_name = "FreeRadio-TimeShiftCaptureHLS" if self._is_hls else "FreeRadio-TimeShiftCapture"
		self._thread = threading.Thread(
			target=target, args=(my_gen,), name=thread_name, daemon=True,
		)
		self._thread.start()

	def stop(self):
		"""Stop capturing and remove the buffer file."""
		self._stop_event.set()
		thread = self._thread
		if thread and thread.is_alive():
			thread.join(timeout=5)
		self._thread = None
		self._active = False
		self._close_file_handle()
		path = self._file_path
		self._file_path = None
		if path:
			try:
				os.remove(path)
			except OSError:
				pass

	def is_active(self):
		return self._active

	def is_hls_skipped(self):
		"""True only if the current/last station is an HLS (.m3u8) stream
		whose manifest could not be read at all on the very first attempt
		(bad URL, DNS/network failure, etc.) - i.e. capture never managed
		to buffer a single byte. HLS streams that read fine are captured
		normally and this returns False for them, same as plain HTTP."""
		return self._hls_skipped

	def get_file_path(self):
		return self._file_path

	def buffered_seconds(self):
		"""Rough estimate of how much audio is currently available in the
		buffer, i.e. how far back the user can rewind."""
		if not self._session_start:
			return 0.0
		elapsed = time.time() - self._session_start
		return max(0.0, min(elapsed, self.CAPACITY_SECONDS + self._TRIM_MARGIN_SECONDS))

	def enter_playback(self):
		"""Called when a time-shift playback session starts reading the
		buffer file. Suspends trimming until exit_playback() is called so
		the file is not modified out from under the open BASS file stream.
		"""
		self._suspend_trim = True

	def exit_playback(self):
		"""Called when a time-shift playback session ends (user returned
		to live). Trimming resumes on the next capture-loop check.
		"""
		self._suspend_trim = False

	# -- Internal -------------------------------------------------------

	def _close_file_handle(self):
		with self._file_lock:
			if self._file_handle:
				try:
					self._file_handle.close()
				except Exception:
					pass
				self._file_handle = None

	def _is_stale(self, my_gen):
		"""True if a newer start() call has superseded the session this
		capture thread was launched for - it should exit immediately."""
		return my_gen != self._generation

	def _run(self, my_gen):
		"""Capture loop: connects to the stream (plain HTTP, falling back to
		a raw-socket ICY connection for Shoutcast-style servers - the same
		approach recorder.py uses), appends raw bytes to the buffer file,
		and periodically trims the front of the file to respect
		CAPACITY_SECONDS while no time-shift playback session is active.

		*my_gen* is checked on every iteration - if a newer station has
		started in the meantime, this loop exits immediately regardless of
		whether stop() was called, so a stale capture can never linger.
		"""
		url = self._url
		try:
			if self._is_stale(my_gen):
				return

			reader = None
			is_socket = False
			try:
				req = urllib.request.Request(
					url,
					headers={"User-Agent": _recorder_mod._USER_AGENT, "Icy-MetaData": "0"},
				)
				reader = _recorder_mod._urlopen(req, 20)
			except Exception as e:
				if not _recorder_mod._is_icy_error(e):
					log.warning("FreeRadio TimeShift: connection failed: %s", e)
					return
				try:
					sock, _headers, prefix = _recorder_mod._open_icy(url, timeout=20)
				except Exception as e2:
					log.warning("FreeRadio TimeShift: ICY connection failed: %s", e2)
					return
				reader = sock
				is_socket = True
				if prefix and not self._is_stale(my_gen):
					self._write_chunk(prefix, my_gen)

			if self._is_stale(my_gen):
				try:
					reader.close()
				except Exception:
					pass
				return

			if is_socket:
				log.info("FreeRadio TimeShift: capture connected via raw ICY socket for %s", url)
			else:
				log.info("FreeRadio TimeShift: capture connected via HTTP for %s", url)

			last_trim_check = time.time()
			chunk_count = 0

			while not self._stop_event.is_set() and not self._is_stale(my_gen):
				try:
					chunk = reader.recv(_CHUNK) if is_socket else reader.read(_CHUNK)
				except Exception as e:
					log.warning("FreeRadio TimeShift: capture read failed after %d chunk(s): %s",
								 chunk_count, e)
					break
				if not chunk:
					log.info("FreeRadio TimeShift: capture stream ended (server closed connection) "
							  "after %d chunk(s)", chunk_count)
					break
				chunk_count += 1
				self._write_chunk(chunk, my_gen)

				now = time.time()
				if now - last_trim_check >= self._TRIM_CHECK_INTERVAL:
					last_trim_check = now
					if not self._suspend_trim:
						self._maybe_trim(my_gen)

			log.info("FreeRadio TimeShift: capture loop exiting, wrote %d chunk(s), "
					  "%d byte(s) total", chunk_count, self._bytes_written)
			try:
				reader.close()
			except Exception:
				pass
		except Exception as e:
			log.warning("FreeRadio TimeShift: capture loop failed: %s", e, exc_info=True)
		finally:
			# Only close/clear the handle if we are still the current
			# session - a newer start() may already own a different handle.
			if not self._is_stale(my_gen):
				self._close_file_handle()

	def _run_hls(self, my_gen):
		"""Capture loop for HLS (.m3u8) stations.

		Resolves the master playlist down to the highest-bandwidth media
		playlist (same approach as recorder.py's HLS recording path),
		then polls it for new segments and downloads them in order,
		appending each segment's raw bytes to the buffer file via
		_write_chunk() - the exact same mechanism the plain-HTTP path
		uses. From bass_host.py's point of view the resulting buffer file
		is indistinguishable from a plain-HTTP capture.

		fMP4-packaged streams additionally carry a one-time #EXT-X-MAP
		initialization segment; it is written once, right at the start of
		the buffer, and its length is recorded in _reserved_prefix_len so
		_maybe_trim() never trims it away.

		*my_gen* is checked throughout exactly as in _run() - a newer
		station superseding this one makes the loop exit immediately.
		"""
		import re as _re
		from urllib.parse import urljoin

		def _abs(u, base_url):
			return urljoin(base_url, u)

		manifest_url = self._url
		seen_segments = set()
		manifest_attempts = 0
		first_segment_written = False
		last_map_url = None
		last_trim_check = time.time()
		chunk_count = 0

		log.info("FreeRadio TimeShift: HLS capture started for %s", manifest_url)

		try:
			while not self._stop_event.is_set() and not self._is_stale(my_gen):
				try:
					base_url = manifest_url.rsplit("/", 1)[0] + "/"
					req = urllib.request.Request(
						manifest_url, headers={"User-Agent": _recorder_mod._USER_AGENT},
					)
					with _recorder_mod._urlopen(req, 10) as resp:
						text = resp.read(32768).decode("utf-8", errors="ignore")
					lines = text.splitlines()
					manifest_attempts = 0
				except Exception as e:
					manifest_attempts += 1
					log.warning("FreeRadio TimeShift: HLS manifest fetch failed (attempt=%d): %s",
								 manifest_attempts, e)
					if not first_segment_written:
						# Never managed to read the manifest at all - treat
						# this station as genuinely unsupported rather than
						# retrying forever with nothing ever buffered.
						self._hls_skipped = True
						return
					if self._is_stale(my_gen) or self._stop_event.wait(4):
						return
					continue

				if self._is_stale(my_gen):
					return

				# Master playlist? Switch to the highest-bandwidth sub-manifest.
				best_manifest, best_bw = None, -1
				for i, line in enumerate(lines):
					if line.startswith("#EXT-X-STREAM-INF"):
						m = _re.search(r"BANDWIDTH=(\d+)", line, _re.IGNORECASE)
						bw = int(m.group(1)) if m else 0
						if i + 1 < len(lines):
							nxt = lines[i + 1].strip()
							if nxt and bw > best_bw:
								best_bw, best_manifest = bw, _abs(nxt, base_url)
				if best_manifest and best_manifest != manifest_url:
					log.info("FreeRadio TimeShift: HLS -> best sub-manifest (bw=%d): %s",
							  best_bw, best_manifest)
					manifest_url = best_manifest
					continue

				# #EXT-X-MAP initialization segment (required for fMP4 streams).
				current_map_url = None
				for line in lines:
					line_s = line.strip()
					if line_s.startswith("#EXT-X-MAP:"):
						m = _re.search(r'URI="([^"]+)"', line_s)
						if m:
							current_map_url = _abs(m.group(1), base_url)
						break

				new_segments = []
				for line in lines:
					line = line.strip()
					if line and not line.startswith("#"):
						seg_url = _abs(line, base_url)
						if seg_url not in seen_segments:
							new_segments.append(seg_url)

				for seg_url in new_segments:
					if self._stop_event.is_set() or self._is_stale(my_gen):
						return
					seen_segments.add(seg_url)

					if current_map_url and current_map_url != last_map_url:
						try:
							map_req = urllib.request.Request(
								current_map_url, headers={"User-Agent": _recorder_mod._USER_AGENT},
							)
							with _recorder_mod._urlopen(map_req, 15) as map_resp:
								init_data = map_resp.read()
							self._write_chunk(init_data, my_gen)
							with self._file_lock:
								self._reserved_prefix_len += len(init_data)
							last_map_url = current_map_url
							log.info("FreeRadio TimeShift: wrote fMP4 init segment (%d bytes)",
									  len(init_data))
						except Exception as e:
							log.warning("FreeRadio TimeShift: failed to fetch init segment: %s", e)

					try:
						seg_req = urllib.request.Request(
							seg_url, headers={"User-Agent": _recorder_mod._USER_AGENT},
						)
						with _recorder_mod._urlopen(seg_req, 15) as seg_resp:
							data = seg_resp.read()
					except Exception as e:
						log.warning("FreeRadio TimeShift: segment download failed: %s", e)
						continue

					if self._is_stale(my_gen):
						return
					self._write_chunk(data, my_gen)
					first_segment_written = True
					chunk_count += 1

					now = time.time()
					if now - last_trim_check >= self._TRIM_CHECK_INTERVAL:
						last_trim_check = now
						if not self._suspend_trim:
							self._maybe_trim(my_gen)

				if len(seen_segments) > 500:
					# Bound memory on long-running sessions; the live edge
					# has long since moved past these, so they're safe to drop.
					seen_segments = set(list(seen_segments)[-200:])

				if self._stop_event.wait(4):
					return

			log.info("FreeRadio TimeShift: HLS capture loop exiting, wrote %d segment(s), "
					  "%d byte(s) total", chunk_count, self._bytes_written)
		except Exception as e:
			log.warning("FreeRadio TimeShift: HLS capture loop failed: %s", e, exc_info=True)
		finally:
			if not self._is_stale(my_gen):
				self._close_file_handle()

	def _write_chunk(self, data, my_gen):
		if not data or self._is_stale(my_gen):
			return
		path = self._file_path
		if not path:
			return
		with self._file_lock:
			if self._is_stale(my_gen):
				return
			try:
				if self._file_handle is None:
					self._file_handle = open(path, "ab", buffering=0)
				self._file_handle.write(data)
				self._bytes_written += len(data)
			except OSError as e:
				log.warning("FreeRadio TimeShift: write failed: %s", e)

	def _maybe_trim(self, my_gen):
		"""Drop the oldest portion of the buffer file once it exceeds
		CAPACITY_SECONDS + margin, estimated from the average byte rate
		observed so far in this session."""
		if self._is_stale(my_gen):
			return
		if not self._session_start:
			return
		elapsed = time.time() - self._session_start
		if elapsed <= self.CAPACITY_SECONDS + self._TRIM_MARGIN_SECONDS:
			return
		if self._bytes_written <= 0 or elapsed <= 0:
			return

		bytes_per_second = self._bytes_written / elapsed
		keep_bytes = int(bytes_per_second * self.CAPACITY_SECONDS)

		path = self._file_path
		if not path:
			return

		with self._file_lock:
			if self._is_stale(my_gen):
				return
			try:
				# Close the persistent handle before rewriting the file, and
				# reopen it afterwards - trimming is infrequent (every ~2
				# min over capacity) so this brief close/reopen is cheap
				# compared to reopening on every chunk.
				if self._file_handle:
					try:
						self._file_handle.close()
					except Exception:
						pass
					self._file_handle = None

				size = os.path.getsize(path)
				prefix_len = min(self._reserved_prefix_len, size)
				trimmable = size - prefix_len
				if trimmable <= keep_bytes:
					self._file_handle = open(path, "ab", buffering=0)
					return
				drop_bytes = trimmable - keep_bytes
				with open(path, "rb") as f:
					prefix = f.read(prefix_len) if prefix_len else b""
					f.seek(prefix_len + drop_bytes)
					remainder = f.read()
				with open(path, "wb") as f:
					if prefix:
						f.write(prefix)
					f.write(remainder)
				# Nudge the session start forward so buffered_seconds() stays
				# roughly accurate after trimming. Only the trimmed (non-
				# reserved) portion represents elapsed playback time.
				self._session_start += drop_bytes / bytes_per_second
				self._bytes_written = len(prefix) + len(remainder)
				self._file_handle = open(path, "ab", buffering=0)
			except OSError as e:
				log.warning("FreeRadio TimeShift: trim failed: %s", e)
				try:
					self._file_handle = open(path, "ab", buffering=0)
				except OSError:
					self._file_handle = None
