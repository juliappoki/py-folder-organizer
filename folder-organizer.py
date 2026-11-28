from pathlib import Path
from collections import defaultdict

EXTENSION_DICT = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".jfif": "Images",
    ".heic": "Images",

    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".wmv": "Videos",

    ".mp3": "Audio",
    ".aac": "Audio",
    ".m4a": "Audio",
    ".opus": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",

    ".pdf": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".csv": "Documents",
    ".xsls": "Documents",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    ".exe": "Executables",
    ".msi": "Executables",
}

def parser(filePaths: Path) -> dict[str, list[Path]]:
    groupsDict = defaultdict(list)

    for item in filePaths.rglob("*"):
        if not item.is_file():
            continue

        categories = EXTENSION_DICT.get(item.suffix.lower(), "Miscellaneous")
        groupsDict[categories].append(item)

    return groupsDict


if __name__ == "__main__":

    rawPath = input("Type the directory/folder you would like to tidy up: ").strip().strip("'").strip('"')
    filePaths = Path(rawPath)

    totalForEach = parser(filePaths)
    counter = {key: len(value) for key, value in totalForEach.items()}

    print(counter)