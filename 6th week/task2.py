def factors(n):
    if n == 0:
        raise ValueError("0 has infinitely many factors")
    n = abs(n)
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result
num = int(input("Enter an integer: "))
print("Factors:", factors(num))
