"""
10.Write a program that takes a distance in kilometers and converts it to miles, displaying the result
 with exactly three decimal places.
"""


distance=float(input("Enter the distance in kilometer: "))

mile=0.621371*distance

print(f"{distance} Km is equivalent to {round(mile,3) } mile")