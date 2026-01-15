from collections import Counter
def six_most_common_letters(message):
    letters = [char.lower() for char in message if char.isalpha()]
    letter_counts = Counter(letters)
    most_common_six = letter_counts.most_common(6)
    for letter, count in most_common_six:
        print(f"{letter}: {count}")
if __name__ == "__main__":
    test_message = "I love my motherland."
    six_most_common_letters(test_message)
