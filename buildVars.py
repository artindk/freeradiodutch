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
	addon_version="2026.19.4",
	
	# Brief changelog for this version
	# Translators: what's new content for the add-on version
	addon_changelog=_("""
**Focus management after item removal**
- Favorites list: after deleting a station, focus and selection automatically move to the next item in the list. If the deleted station was the last one, focus moves to the previous item. If the list becomes empty, focus moves to the Play button.
- Liked Songs list: same behaviour — after removing a song, focus stays on the next item, or moves to the Refresh button if the list is empty.
**Delete key shortcut**
- Pressing `Delete` while a station is selected in the Favorites list now triggers the Delete Station button (equivalent to clicking it), provided the button is enabled.
- Pressing `Delete` while a song is selected in the Liked Songs list now triggers the Remove button, provided the button is enabled.
- In both cases the key has no effect when no valid item is selected or the corresponding button is disabled.
- Added a new "Mute notifications" checkbox to FreeRadio settings (unchecked by default).
- When enabled, NVDA no longer announces station changes, playback state changes (play, pause, stop), or recording events (started, stopped, finished).
- Error messages, favourites feedback, music recognition results, and update notifications are intentionally unaffected.
- Added an unassigned script_toggleMuteNotifications input gesture that toggles the setting on the fly. Assign a key combination via NVDA's Input Gestures dialog under the FreeRadio category.
- Two module-level helpers (_notify, _notify_on_demand) centralise the mute check, keeping call sites clean.
**Changed: Search now filters by selected country automatically**
- Search queries are now scoped to the selected country. When a country is chosen in the combo box, results are fetched from the API already filtered by that country rather than searching globally and filtering locally afterward.
- The Search button has been removed. Results update automatically as you type (debounced, 500 ms delay), so a manual trigger is no longer needed.
- Removed the Enter key and Alt+A shortcuts that previously triggered a manual search.
- The search status message has been shortened. It now reads `"query": N in Country` instead of the previous `Search "query": N results (N in Country)`.
- The key used for reordering favorites was changed from X to * (star).
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
	addon_lastTestedNVDAVersion="2026.1.0",
	
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