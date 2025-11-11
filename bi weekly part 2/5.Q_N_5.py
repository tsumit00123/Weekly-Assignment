"""
5.Write a program that accepts three numbers from the user and prints the largest among them
"""


a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))


if a>b and a>c:
    print("a is the largest number.")
elif b>a and b>c:
    print("b is the largest number.")
else:
    print("c is the largest number.")