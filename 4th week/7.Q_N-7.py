"""
Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean

"""

temperatures=[]

for i in range(5):
    temp=input(f"Enter the temperature {i}: ")
    if temp[:-1].lower()=="c" or "f":
        temp_value=float(temp[:-1])
        temperatures.append(temp_value)

        


print(f"The maximum temperature is: {max(temperatures)}")
print(f"The minimum temperature is : {min(temperatures)}")

sum=0
for temperature in temperatures:
    sum+=temperature

print(f"The mean temperature is: {sum/6}")










