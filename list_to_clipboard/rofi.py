import subprocess

from list_to_clipboard.types import EntryList

ENTRY_SEPARATOR = "\n"
DISPLAY_SEPARATOR = " - "
OPTION_START = "\0"
OPTION_SEPARATOR = "\x1f"


def read_input(prompt, placeholder):
    theme_str = "entry {{ placeholder: \"{}\"; }} listview {{ enabled: false;}}".format(placeholder)
    result = subprocess.run(
        ["rofi", "-dmenu", "-p", prompt, "-theme-str", theme_str],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )
    return result.returncode, result.stdout.strip()


def file_browser():
    result = subprocess.run(
        [
            "rofi",
            "-show",
            "filebrowser",
            "-filebrowser-command",
            "echo",
            "-filebrowser-cancel-returns-1",
            "true",
        ],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    return result.returncode, result.stdout.strip()


def run(entries: EntryList):

    input = ""
    for entry in entries:
        input += (
            entry.value
            + OPTION_START
            + "display"
            + OPTION_SEPARATOR
            + entry.display_text
            + OPTION_SEPARATOR
            + "meta"
            + OPTION_SEPARATOR
            + entry.display_text
            + ENTRY_SEPARATOR
        )

    result = subprocess.run(
        ["rofi", "-dmenu", "-i", "-no-custom", "-p", "Select entry"],
        input=input,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )

    return result.returncode, result.stdout.strip()
