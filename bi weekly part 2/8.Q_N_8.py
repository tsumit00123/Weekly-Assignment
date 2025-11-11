"""
8.Write a program to take a character input and display whether it is a vowel or consonant.
"""

vowel="aeiouAEIOU"

character=input("Enter a character: ")

if character in vowel:
    print("Vowel")

else:
    print("Consonant")