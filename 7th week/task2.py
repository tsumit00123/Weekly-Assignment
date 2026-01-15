def unique_sorted_letters(word):
    return sorted(set(char.lower() for char in word if char.isalpha()))
def letters_in_either(word1, word2):
    return sorted(set(unique_sorted_letters(word1)) | set(unique_sorted_letters(word2)))
def letters_in_both(word1, word2):
    return sorted(set(unique_sorted_letters(word1)) & set(unique_sorted_letters(word2)))
def letters_in_one_only(word1, word2):
    return sorted(set(unique_sorted_letters(word1)) ^ set(unique_sorted_letters(word2)))
if __name__ == "__main__":
    w1 = "cheese"
    w2 = "cheddar"
    print("Either:", letters_in_either(w1, w2))
    print("Both:", letters_in_both(w1, w2))
    print("One only:", letters_in_one_only(w1, w2))
