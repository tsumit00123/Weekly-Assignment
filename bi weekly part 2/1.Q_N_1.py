"""
1.Write a program to take a number input from the user and display whether the number is positive, negative, or zero.

"""


while True:
    try:
        num=int(input("Enter a number: "))
        break
    except ValueError as e:
        print("Invalid input. Please try again!")

if num>0:
    print(f"{num} is positive number: ")

elif num<0:
    print(f"{num} is negitive number")

else:
    print(f"{num} is Zero")