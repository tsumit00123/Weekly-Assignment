"""
3.Write a program to convert Fahrenheit to Celsius and display the result rounded to two decimal places.

"""

temperature=float(input("Enter a temperature in (degree Fahrenheit):  "))
degree_celcius=(temperature-32)*(5/9)
print(f"{temperature}F is equivalent to {round(degree_celcius,2)}C")