def unique_sorted_letters(s):
    letters = [char for char in s if char.isalpha()]
    unique_letters = set(letters)
    return sorted(unique_letters)
if __name__ == "__main__":
    test_string = "cheese"
    print(unique_sorted_letters(test_string))  