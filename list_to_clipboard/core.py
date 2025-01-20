from pathlib import Path

import pyperclip

from list_to_clipboard import (HISTORY_FILE, MAX_HISTORY, OPERATIONS, OPERATIONS_ID,
                               SETTINGS_DIR, rofi)
from list_to_clipboard.file_history import add_history_entry, get_recent_file
from list_to_clipboard.types import Entry, EntryList


def _init(settings_dir: Path, history_file: Path):
    settings_dir.mkdir(parents=True, exist_ok=True)
    if not history_file.is_file():
        with open(history_file, "a"):
            return


def select_file():
    return_code, file = rofi.file_browser()
    if not Path(file) or return_code == 1:
        return None
    return Path(file)


def read_file(filename, desc_separator) -> EntryList:
    list = []
    with open(filename) as file:
        for line in file:
            value, description = line.rstrip().split(desc_separator, 1)
            display_text = value + " - " + description
            entry = Entry._make((value, description, display_text))
            list.append(entry)

    return list


def handle_operation(operation_id):
    operation = OPERATIONS_ID.get(operation_id)
    match operation:
        case "select_file":
            print("select")
            pass
        case "add_entry":
            print("add")
            pass
        case "edit_entry":
            print("edit")
            pass
        case "delete_entry":
            print("delete")
            pass
    pass


def main(
    filename=None,
    desc_separator="|||",
):
    _init(SETTINGS_DIR, HISTORY_FILE)

    entry_list = []

    if not filename:
        file = get_recent_file(HISTORY_FILE)
        if not file:
            file = select_file()
            if not file:
                return
        entry_list = read_file(file, desc_separator)
    else:
        file = Path(filename)
        entry_list = read_file(file, desc_separator)

    entry_list.extend(OPERATIONS.values())

    _, selected = rofi.run(entry_list)

    if selected in OPERATIONS_ID.keys():
        handle_operation(selected)
        return

    add_history_entry(file, HISTORY_FILE, MAX_HISTORY)

    pyperclip.copy(selected)
