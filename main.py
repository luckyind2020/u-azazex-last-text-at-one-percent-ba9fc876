import pathlib

ENTRY_FILE = pathlib.Path(__file__).with_name("entry.txt")


def read_entry():
    raw = ENTRY_FILE.read_text(encoding="utf-8")
    message = raw.strip()
    if not message:
        raise ValueError("entry.txt holds no text to send")
    if len(message) > 200:
        raise ValueError("entry is longer than 200 characters")
    return message


def main():
    print(read_entry())


if __name__ == "__main__":
    main()
