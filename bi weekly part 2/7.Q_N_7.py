"""
7.Write a program that takes a temperature in Celsius and prints whether it’s Cold (<10°C), Warm (10–25°C), 
or Hot (>25°C).
"""


temperature=int(input("Enter a temperature in degree celcius: "))


if temperature<10:
    print("Cold")

elif 10<=temperature<=25:
    print("Warm")

else:
    print("Hot")