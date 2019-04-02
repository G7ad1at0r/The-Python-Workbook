import math

radius = float(input("Enter the radius of the cylinder:\n>>> "))
height = float(input("Enter the height of the cylinder:\n>>> "))

volume = height * math.pi * (radius * radius)

print("The volume of the cylinder is %.1f" % volume)