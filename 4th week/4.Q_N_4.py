"""
When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)

"""

def remove_last_character(string):
    str_len=len(string)
    new_string=""
    if str_len<=1:
        return string
    else:
        for i in range(str_len-1):
            new_string+=string[i]
        return new_string
        



string=input("Enter a string: ")
str_len=len(string)


print(f"String after removing last character: {remove_last_character(string)}")



