"""
Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function

"""

def is_integer(num):
    if 0<=num<=100:
        return True
    
    else:
        return False
    

while(True):
    try:
        num=int(input("Enter a number: "))
        print(is_integer(num))
        break


    except ValueError as e:
        print(f"Invalid: {e}")

print("Program End")





