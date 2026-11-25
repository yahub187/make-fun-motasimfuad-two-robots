import os

ENTRY_FILENAME = "entry.txt"

ENTRY_TEXT = "I pressed the door-close button for you. It is disconnected, but the gesture is fully operational."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
