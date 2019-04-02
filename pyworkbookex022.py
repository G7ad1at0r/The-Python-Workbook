print("Triangle Calculator SSS")

from math import sqrt

s1 = float(input("Enter the lenth of side A:\n>>> "))
s2 = float(input("Enter the lenth of side B:\n>>> "))
s3 = float(input("Enter the lenth of side C:\n>>> "))

s = (s1 + s2 + s3) / 2

area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

print("The area of the triangle is", area)