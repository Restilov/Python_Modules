import sys
from typing import IO
 
 
def read_file(filename: str) -> None:
    print(f"Accessing file '{filename}'")
    file: IO[str]
    try:
        file = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    print("---")
    print(file.read(), end="")
    print("\n---")
    file.close()
    print(f"File '{filename}' closed.")
 
 
def main() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    read_file(sys.argv[1])
 
 
main()
