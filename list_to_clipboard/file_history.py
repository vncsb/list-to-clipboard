from pathlib import Path


def add_entry(entry: Path, history_path: Path, max_entries: int):
    entry_line = str(entry.resolve()) + "\n"

    with open(history_path, "r+") as file:
        lines = file.readlines()
        file.truncate(0)
        file.seek(0)

        if entry_line in lines:
            lines.remove(entry_line)
        elif len(lines) == max_entries:
            lines = lines[1:]

        lines.append(entry_line)
        file.writelines(lines)


def get_recent_file(path: Path):
    if path.is_file():
        with open(path, "r") as file:
            return file.readlines()[-1].strip()
    return None
