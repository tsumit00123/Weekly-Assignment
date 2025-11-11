"""
2.Write a program that asks for two integers and displays the remainder and quotient after dividing the
 first by the second.

"""

num1=int(input("Enter a first number: "))
num2=int(input("Enter a second number: "))

reminder=num1%num2
quotient=num1/num2

print(f"Reminder: {reminder}")
print(f"Quotient: {quotient}")