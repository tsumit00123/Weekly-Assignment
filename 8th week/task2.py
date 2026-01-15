import sys
import os
def create_file(filename):
    """Ask user to enter content for a missing file and save it."""
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
def compare_files(file1, file2):
    """Compare two files and report if they are the same or different."""
    if not os.path.exists(file1):
        create_file(file1)
    if not os.path.exists(file2):
        create_file(file2)
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
        if lines1 == lines2:
            print(f"'{file1}' and '{file2}' are the same.")
        else:
            print(f"'{file1}' and '{file2}' are different.")
    except PermissionError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <file1> <file2>")
        sys.exit(1)
    compare_files(sys.argv[1], sys.argv[2])
