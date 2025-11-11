"""
Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).

"""

def celcius_to_fahrenheit(temp1):
    degree_fahrenheit=temp1*(9/5)+32
    return degree_fahrenheit
    

def fahrenheit_to_celcius(temp2):
    degree_celcius=(temp2-32)*(5/9)
    return degree_celcius




print("1. Celcius to Fahrehier")
print("2. Fahrenheit to Celcius")

choice=input("Enter a choice: ")

if choice=="1":
    temp=float(input("Enter the temperature in (degree celcius): "))
    print(f"{temp}C is equivalent to {celcius_to_fahrenheit(temp)}F ")
    

elif choice=="2":
    temp=float(input("Enter a temperature in (degree Fahrenheit):  "))
    degree_celcius=(temp-32)*(5/9)
    print(f"{temp}F is equivalent to {degree_celcius(temp)}C")

else:
    print("Invalid Choice")


