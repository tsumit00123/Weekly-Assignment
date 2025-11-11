
"""
11. Write a program to find the Euclidean distance between two coordinates. Take both the coordinates from 
the user as input.
"""

import math as ma

print("First Cordinate.")
x1=float(input("Enter the value of x1: "))
y1=float(input("Enter the value of y1: "))
print()

print("Second Cordinate. ")
x2=float(input("Enter the value of x2: "))
y2=float(input("Enter the value of y2: "))
print()


Euclidean_distance=ma.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"The Euclidean distance between two cordinates ({x1},{y1}) and ({x2},{y2}) is {Euclidean_distance:.4f}")