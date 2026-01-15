import sys
import os
def simple_wc(filename):
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
        line_count = 0
        char_count = 0
        with open(filename, 'r') as file:
            for line in file:
                line_count += 1
                char_count += len(line)
        print(f"Lines: {line_count}")
        print(f"Characters: {char_count}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <filename>")
        sys.exit(1)
    file_name = sys.argv[1]
    simple_wc(file_name)