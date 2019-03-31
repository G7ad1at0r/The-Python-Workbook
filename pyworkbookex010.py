import math

a = int(input("Enter integer a:\n>>> "))
b = int(input("Enter integer b:\n>>> "))

print("Your intetgers a & b:\na = ", a,"\nb = ", b, "\n")

print(a, " + ", b," = ", a + b)

print(b, " - ", a, " = ", b - a)

print(a, " x ", b, " = ", a * b)

print(a, " ÷ ", b, " = ", a / b)

print(a, " ÷ ", b, "gives the remainder", a % b)

print(a, "log10 = ", math.log10(a))

print(b, "log10 = ", math.log10(b))

print(a, "√", b, " = ", a ** b)