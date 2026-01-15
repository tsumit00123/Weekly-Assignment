import sys
import os
def simple_grep(pattern, filename):
    if not os.path.exists(filename):
        create = input(f"File '{filename}' not found. Do you want to create it? (y/n): ").strip().lower()
        if create == 'y':
            print("Creating the file. Enter content. Finish with an empty line:")
            with open(filename, 'w') as f:
                while True:
                    line = input()
                    if line == "":
                        break
                    f.write(line + '\n')
            print(f"File '{filename}' created.\n")
        else:
            print("Exiting without creating the file.")
            return
    try:
        with open(filename, 'r') as file:
            found = False
            for line in file:
                if pattern in line:
                    print(line, end='')
                    found = True
            if not found:
                print(f"No lines found containing '{pattern}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <pattern> <filename>")
        sys.exit(1)
    search_pattern = sys.argv[1]
    file_name = sys.argv[2]
    simple_grep(search_pattern, file_name)


