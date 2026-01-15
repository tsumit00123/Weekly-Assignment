import sys
import os
import string
def create_dictionary(dict_file="dictionary.txt"):
    """Ask the user to create the dictionary if it does not exist."""
    print(f"Dictionary file '{dict_file}' not found.")
    create = input("Do you want to create it? (y/n): ").strip().lower()
    if create != "y":
        print("Cannot continue without a dictionary. Exiting.")
        sys.exit(1)
    print("Enter dictionary words, one per line. Finish with an empty line:")
    with open(dict_file, "w") as f:
        while True:
            word = input().strip()
            if word == "":
                break
            f.write(word.lower() + "\n")
    print(f"Dictionary '{dict_file}' created.\n")
def create_text_file(filename):
    """Ask the user to create the text file if it does not exist."""
    print(f"File '{filename}' not found.")
    create = input("Do you want to create it? (y/n): ").strip().lower()
    if create != "y":
        print("Cannot continue without a text file. Exiting.")
        sys.exit(1)
    print(f"Enter text content for '{filename}'. Finish with an empty line:")
    with open(filename, "w") as f:
        while True:
            line = input()
            if line == "":
                break
            f.write(line + "\n")
    print(f"File '{filename}' created.\n")
def load_dictionary(dict_file="dictionary.txt"):
    """Load dictionary words into a set."""
    if not os.path.exists(dict_file):
        create_dictionary(dict_file)
    with open(dict_file, "r") as f:
        return set(word.strip().lower() for word in f)
def spell_check(filename, dictionary):
    """Print words from the file that are not in the dictionary."""
    if not os.path.exists(filename):
        create_text_file(filename)
    with open(filename, "r") as f:
        text = f.read().lower()
        # Remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        words = text.split()
    misspelled = set(word for word in words if word not in dictionary)
    if misspelled:
        print("Misspelled words:")
        for word in sorted(misspelled):
            print(word)
    else:
        print("No misspelled words found.")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    dictionary = load_dictionary()
    spell_check(filename, dictionary)
