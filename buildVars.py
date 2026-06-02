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
	addon_version="2026.19.7",
	
	# Brief changelog for this version
	# Translators: what's new content for the add-on version
	addon_changelog=_("""
**New Languages for Freeradio**
- Czech by jiri Holzinger.
- Arabic by ALI ALOMARI
- French and Spanish by Rémy Ruiz
- Khmer by Phearith
- Russian by Валентин Куприянов
**Station Manager: resilient mirror selection**
- The Radio Browser server list is now fetched dynamically via DNS lookup (`all.api.radio-browser.info`) at startup, following the approach recommended by the Radio Browser API. Servers are shuffled before use so load is distributed across the network. When DNS discovery fails, the previous hardcoded mirror list is used as a fallback. Temporary HTTP 5xx errors (e.g. 503 Service Unavailable) are now retried once after a short delay before moving on to the next mirror, reducing failed loads during brief server outages.
**Search: multi-token filtering for All Stations and Favourites**
- Local filtering in both the All Stations tab and the Favourites tab now splits the search query into individual tokens and requires all of them to match (AND logic). For example, searching "jazz france" returns only stations whose metadata contains both "jazz" and "france". The last token is matched as a prefix so that results remain visible while the user is still typing a word. The status label in the All Stations tab now always reflects the actual number of visible stations after filtering, rather than the raw count returned by the API.
- Added a "Result limit" setting to the All Stations tab to control the maximum number of results fetched for searches and country filters.
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