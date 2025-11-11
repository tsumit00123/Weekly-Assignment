"""
Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.

"""

def is_upper_lower(string):
    lower_case=0
    upper_case=0

    for i in string:
        if 'A'<=i<='Z':
            upper_case+=1
        elif 'a'<=i<='z':
            lower_case+=1

    return upper_case,lower_case

    
  
string=input("Enter a single string: " )
upper,lower=is_upper_lower(string)
print(f"The total number of upper case: {upper}")
print(f"The total number of lower case: {lower}")







