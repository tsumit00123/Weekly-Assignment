# Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.


print("1. Celcius to Fahrehier")
print("2. Fahrenheit to Celcius")

choice=input("Enter a choice: ")

if choice=="1":
    temp1=float(input("Enter the temperature in (degree celcius): "))
    degree_fahrenheit=temp1*(9/5)+32
    print(f"{temp1}C is equivalent to {degree_fahrenheit}F ")

elif choice=="2":
    temp2=float(input("Enter a temperature in (degree Fahrenheit):  "))
    degree_celcius=(temp2-32)*(5/9)
    print(f"{temp2}F is equivalent to {degree_celcius}C")

else:
    print("Invalid Choice")
