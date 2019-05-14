print("The Greatest Common Divisor")

n = int(input("Enter a Positive Integer:\n>>> "))
m = int(input("Enter a Positive Integer:\n>>> "))

d = min(n, m)

while n % d != 0 or m % d != 0:
    d = d - 1

print(f"\nThe greatest common divisor of {n} and {m} is: {d}")