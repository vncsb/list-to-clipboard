from pathlib import Path

from list_to_clipboard import HISTORY_FILE, MAX_HISTORY, SETTINGS_DIR, rofi
from list_to_clipboard.file_history import add_entry, get_recent_file
from list_to_clipboard.types import EntryList


def _init(settings_dir: Path, history_file: Path):
    settings_dir.mkdir(parents=True, exist_ok=True)
    if not history_file.is_file():
        with open(history_file, "a"):
            return


def read_file(filename, desc_separator):
    list = []
    with open(filename) as file:
        for line in file:
            [value, description] = line.rstrip().split(desc_separator, 1)
            list.append((value, description))

    rofi.run(list)


def main(
    filename=None,
    parsed_list: EntryList = [],
    desc_separator="|||",
):
    _init(SETTINGS_DIR, HISTORY_FILE)

    if not filename and not parsed_list:
        last_file = get_recent_file(HISTORY_FILE)
        if not last_file:
            print("fudeuuuu")
            exit()
        read_file(last_file, desc_separator)

    if filename:
        path = Path(filename)
        read_file(path, desc_separator)
        add_entry(path, HISTORY_FILE, MAX_HISTORY)

    pass
