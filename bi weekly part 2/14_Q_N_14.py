"""
14.Write a Python program that accepts a string and calculates the number of digits and letters. 
"""

string=input("Enter the string: ")
i=0
digit=0
letter=0

while i<len(string):
    if string[i].isdigit():
        digit+=1

    else:
        letter+=1

    i+=1

print(f"The total no of digits in {string} is {digit}")
print(f"The total no of digits in {string} is {letter}")