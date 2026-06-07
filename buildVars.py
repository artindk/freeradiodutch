# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _

# Add-on information variables
addon_info = AddonInfo(
	# add-on Name/identifier, internal for NVDA
	addon_name="freeradio",
	
	# Add-on summary/title, usually the user visible name of the add-on
	# Translators: Summary/title for this add-on
	addon_summary=_("freeRadio"),
	
	# Add-on description
	# Translators: Long description to be shown for this add-on
	addon_description=_("""FreeRadio is an internet radio add-on for NVDA that provides seamless access to thousands of stations via the Radio Browser open directory. It features a fully accessible station browser with search, country filter, favourites management, and per-station audio profiles. Playback is handled by a prioritised backend chain (BASS, VLC, PotPlayer, Windows Media Player) with support for volume control, audio effects, output device selection, and simultaneous audio mirroring to a second device. Additional features include instant and scheduled recording, sleep and alarm timers, automatic ICY metadata announcements, Shazam-based music recognition, and a liked-songs log. All controls and shortcuts are designed for NVDA accessibility."""),
	
	# version
	addon_version="2026.19.8",
	
	# Brief changelog for this version
	# Translators: what's new content for the add-on version
	addon_changelog=_("""
- Fixed playback of HTTPS Icecast streams that caused BASS to fail with
  BASS_ERROR_FILEFORM (err=40). Affected streams sent ICY response headers
  immediately after the TLS handshake, before a standard HTTP status line,
  which BASS's SSL layer could not parse.
- Implemented a local loopback proxy in bass_host.py to work around the
  issue: urllib opens the HTTPS connection (which tolerates ICY quirks),
  and BASS reads plain HTTP audio from a localhost socket instead.
- The remote HTTPS connection and BASS's local connect now happen in
  parallel, keeping startup latency close to that of a normal stream.
- ICY headers (content-type, icy-metaint, icy-br, icy-sr, etc.) are
  forwarded accurately from the remote server to BASS. Previously sending
  icy-metaint: 0 caused garbled audio and a phaser/chorus-like artifact.
- Removed the _BASS_SKIP_HOSTS workaround in radioPlayer.py that
  bypassed BASS entirely for icecast.walmradio.com, restoring full BASS
  features (ICY metadata, bass boost, FX, volume mixer entry) for that
  station.
---
**New: Adjustable EQ Effect Levels**
The Bass Boost, Treble Boost, and Vocal Boost effects now include individual gain controls. When one of these effects is enabled, a dB slider appears next to it, letting you fine-tune the intensity from −15 dB to +15 dB.
Previously, each EQ effect had a fixed strength (Bass: +9 dB, Treble: +9 dB, Vocal: +6 dB). These defaults are unchanged — the controls simply let you go lower or higher as needed.
**What's new:**
- Gain controls appear automatically when an EQ effect is turned on, and hide when it is turned off.
- Values are saved globally and restored when the add-on starts.
- If you save an audio profile for a favourite station, the EQ gain levels are included in that profile and restored whenever you tune to that station.
"""),
	
	# Author(s)
	addon_author="Çağrı Doğan <cagrid@hotmail.com>",
	
	# URL for the add-on documentation support
	addon_url="https://github.com/Surveyor123/freeradio",
	
	# URL for the add-on repository where the source code can be found
	addon_sourceURL="https://github.com/Surveyor123/freeradio",
	
	# Documentation file name
	addon_docFileName="readme.html",
	
	# Minimum NVDA version supported
	addon_minimumNVDAVersion="2024.1.0",
	
	# Last NVDA version supported/tested
	addon_lastTestedNVDAVersion="2026.1.1",
	
	# Add-on update channel (None denotes stable releases)
	addon_updateChannel=None,
	
	# Add-on license
	addon_license="GPL-2.0",
	addon_licenseURL=None,
)

# Define the python files that are the sources of your add-on.
# We point to the specific directory where your code lives.
pythonSources: list[str] = ["addon/globalPlugins/freeradio/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources: list[str] = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
excludedFiles: list[str] = []

# Base language for the NVDA add-on
# Since your code strings (e.g. _("Table")) are in English, we keep this as "en".
baseLanguage: str = "en"

# Markdown extensions for add-on documentation
markdownExtensions: list[str] = []

# Custom braille translation tables
brailleTables: BrailleTables = {}

# Custom speech symbol dictionaries
symbolDictionaries: SymbolDictionaries = {}