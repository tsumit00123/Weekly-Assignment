import sys
args = sys.argv[1:]
if not args:
    print("No temperature readings provided. Please enter values as command-line arguments.")
    sys.exit(1)
try:
    temps = [float(x) for x in args]
except ValueError:
    print("All arguments must be numbers.")
    sys.exit(1)
max_temp = max(temps)
min_temp = min(temps)
mean_temp = sum(temps) / len(temps)
print(f"Maximum temperature: {max_temp}")
print(f"Minimum temperature: {min_temp}")
print(f"Mean temperature: {mean_temp}")
