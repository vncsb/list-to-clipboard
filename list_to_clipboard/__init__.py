from pathlib import Path

SETTINGS_DIR = Path.joinpath(Path.home(), ".local/share/l2c/")
HISTORY_FILE = Path.joinpath(SETTINGS_DIR, "recent_files")
OPTIONS_FILE = Path.joinpath(SETTINGS_DIR, "options")
MAX_HISTORY = 10
