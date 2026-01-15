table = int(input("Enter the number for the times table (0-12, negative for reverse): "))
if abs(table) > 12:
    print("Error: Number must be between -12 and 12")
else:
    if table >= 0:
        for i in range(13):
            print(f"{i} x {table} = {i * table}")
    else:
        table = abs(table)
        for i in range(12, -1, -1):
            print(f"{i} x {table} = {i * table}")
