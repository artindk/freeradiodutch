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
	addon_version="2026.19.6",
	
	# Brief changelog for this version
	# Translators: what's new content for the add-on version
	addon_changelog=_("""
**Liked Songs: duplicate detection**
- Before adding a track to `likedSongs.txt`, the file is now read and checked for an existing entry with the same text. If the track is already present, it is not written again and NVDA announces "Already in liked songs: [track]" instead. This prevents the list from accumulating repeated entries when the same track is recognised or copied multiple times during a session.
**F2 in station browser: 4-press behaviour now mirrors Ctrl+Win+I**
- The in-dialog F2 handler (`_whats_playing_from_dialog`) has been rewritten to match `script_whatsPlaying` press-for-press:
- **1×** — announce the currently playing station and track
- **2×** — open the station details dialog (delayed 350 ms so a 3rd press can cancel it)
- **3×** — copy ICY track title to clipboard; fall back to Shazam if no metadata is available
- **4×** — force Shazam music recognition regardless of ICY metadata, then reset the counter
- Previously the handler merged the 3rd and all subsequent presses into a single `elif count >= 2` branch, so the 4th press was never reached. A cancellation token is now also passed into the 3rd-press background thread so that a 4th press arriving while the thread is still running correctly aborts the clipboard/Shazam action before the forced-recognition path takes over.
**Music Recognizer: improved recognition of non-mainstream tracks**
- Previously, the signature generator stopped processing audio after ~3.1 seconds or 255 peaks, whichever came first. The full 12-second audio sample is now used to build the fingerprint, sending significantly richer data to Shazam. This hopefully improves recognition accuracy for folk, regional, and other non-mainstream music.
**All Stations tab: Sort combo box**
- Added a *Sort* combo box to the All Stations tab, placed before the Country filter. Options are **Alphabetical** (default) and **By Rating** (sorted by vote count, highest first). Changing the sort order instantly re-sorts the current station list without triggering a new network request.
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