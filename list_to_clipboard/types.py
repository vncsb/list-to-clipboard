from typing import NamedTuple

Entry = NamedTuple(
    "Entry", (("value", str), ("description", str), ("display_text", str))
)

EntryList = list[Entry]
