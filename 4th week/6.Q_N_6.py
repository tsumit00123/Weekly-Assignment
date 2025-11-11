"""
Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.

"""


temp=input("Enter the temperature in (degree celcius) : ")
if temp[-1].lower()=='c':
    temp_value=float(temp[:-1])
    degree_fahrenheit=temp_value*(9/5)+32
    print(f"{temp} is equivalent to {degree_fahrenheit}F ")

else:
    print("please enter 'c ' followed by input")