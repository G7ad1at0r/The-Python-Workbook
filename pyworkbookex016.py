from fractions import Fraction

r = float(input("Enter Radius:\n>>> "))
#area = πr2
area = 3.14 * r **2

print("Area is:", area)
#volume = 4/3 πr3
f = Fraction(4,3)

volume = f * 3.14 * r**3

print("Volume is:", volume)