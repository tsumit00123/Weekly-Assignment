import sys
import os
def nl(filename):
    """Print the contents of the file with line numbers."""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        print("Please enter the content for the file. End input with an empty line.")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line + "\n")
        with open(filename, 'w') as f:
            f.writelines(lines)
        print(f"File '{filename}' created.\n")
    try:
        with open(filename, 'r') as file:
            for lineno, line in enumerate(file, start=1):
                print(f"{lineno}\t{line}", end='')
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.", file=sys.stderr)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename> [filename2 ...]", file=sys.stderr)
        sys.exit(1)
    for filename in sys.argv[1:]:
        nl(filename)
