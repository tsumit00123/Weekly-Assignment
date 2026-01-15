def to_binary(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
num = int(input("Enter a positive integer: "))
print("Binary representation:", to_binary(num))

