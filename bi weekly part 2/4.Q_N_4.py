"""
4.Write a program that prompts the user for an age, and prints whether the person is a child (below 13),
 teenager (13–19), or adult (20 and above).
"""

while True:
    try:
        age=int(input("Enter you age: "))
        break
    except ValueError:
        print("Invalid age. Please try again!")

if age<13:
    print("Child")
elif 13<=age<=19:
    print("Teenager")
else:
    print("Adult")

