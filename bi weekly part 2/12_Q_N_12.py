"""
12.Write a program to find the simple interest when the value of principle, rate of interest and time period 
is provided by the user.
"""

p=int(input("Enter the principle: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the time periode : "))

simple_intrest=(p*r*t)/100
print(f"The simple interst is {simple_intrest}")