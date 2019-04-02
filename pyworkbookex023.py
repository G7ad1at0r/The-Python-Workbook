import math

print("THE REGULAR POLYGON AREA CALCULATOR\n")

s = float(input("Enter the lenth of one side of the Polygon:\n>>> "))

n = int(input("Enter the number of sides:\n>>> "))

area = (n * (s * s)) / (4 * math.tan(math.pi / n))

print("The area of the Regualar Polygon with", n,"sides is:\n%.2f" % area, " units.")