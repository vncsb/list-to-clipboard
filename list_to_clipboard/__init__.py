from pathlib import Path

from list_to_clipboard.types import Entry

SETTINGS_DIR = Path.joinpath(Path.home(), ".local/share/l2c/")
HISTORY_FILE = Path.joinpath(SETTINGS_DIR, "recent_files")
OPTIONS_FILE = Path.joinpath(SETTINGS_DIR, "options")
MAX_HISTORY = 10

OPERATIONS: dict[str, Entry] = {
    "select_file": Entry._make(
        (
            "7b95a3c7-902c-4fe9-848c-9850b9f52330",
            "Select another file to be read",
            "Select file - Select another file to be read",
        )
    ),
    "add_entry": Entry._make(
        (
            "44687a57-0ea2-4734-8992-149542224984",
            "Add an entry to this file",
            "Add entry - Add an entry to this file",
        )
    ),
    # "edit_entry": Entry._make(
    #     (
    #         "39a138c9-9649-41af-8f66-fe754f3a7f05",
    #         "Edit an entry in this file",
    #         "Edit entry - Edit an entry in this file",
    #     )
    # ),
    # "delete_entry": Entry._make(
    #     (
    #         "eb9cb004-0f37-4166-b57a-1dd7430a8e7e",
    #         "Delete and entry in this file",
    #         "Delete entry - Delete and entry in this file",
    #     )
    # ),
}

OPERATIONS_ID = {
    "7b95a3c7-902c-4fe9-848c-9850b9f52330": "select_file",
    "44687a57-0ea2-4734-8992-149542224984": "add_entry",
    "39a138c9-9649-41af-8f66-fe754f3a7f05": "edit_entry",
    "eb9cb004-0f37-4166-b57a-1dd7430a8e7e": "delete_entry",
}
