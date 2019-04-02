from math import sqrt

print("How Fast Is An Objects Speed When \nIt Hits The Ground.\n")
distance = float(input("Enter The Height In Meters:\n>>> "))

# initial speed (free fall = 0**2)
x = int(input("Initial Speed:\n>>> "))
vi = x**2

# gravity 9.8 m/s2
acceleration = 9.8

vf = sqrt(vi + 2 * acceleration * distance)

print("The Object Is Travelling At", vf, "\nMeters Per Second.")