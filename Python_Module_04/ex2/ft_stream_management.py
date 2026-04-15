import sys
from typing import IO


def read_file(filename: str) -> str:
    print(f"Accessing file '{filename}'")
    file: IO[str]
    try:
        file = open(filename, "r")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        return ""
    content: str = file.read()
    print("---")
    print(content, end="")
    print("\n---")
    file.close()
    print(f"File '{filename}' closed.")
    return content


def transform_content(content: str) -> str:
    lines: list[str] = content.splitlines()
    new_lines: list[str] = [line + "#" for line in lines]
    return "\n".join(new_lines) + "\n"


def save_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    file: IO[str]
    try:
        file = open(filename, "w")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        print("Data not saved.")
        return
    file.write(content)
    file.close()
    print(f"Data saved in file '{filename}'.")


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    content: str = read_file(sys.argv[1])
    if not content:
        return
    new_content: str = transform_content(content)
    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name: str = sys.stdin.readline().rstrip("\n")
    if not new_name:
        print("Not saving data.")
        return
    save_file(new_name, new_content)


main()
