import subprocess

from list_to_clipboard.types import EntryList

def run(entries: EntryList):

    input = ""
    for value, description in entries:
        input += value + " - " + description + "\n"

    result = subprocess.run(
        ["rofi", "-dmenu"],
        input=input,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    return result.returncode, result.stdout
