print("~~~~Poly Wants A Perimeter~~~~")
print("The Polygon Perimeter Calculator\n")

from math import sqrt

perimeter = 0

first_x = float(input("Enter X Coordinate:\n>>> "))
first_y = float(input("Enter Y Coordinate:\n>>> "))

new_x = first_x
new_y = first_y

line_x = input("Enter X Coordinate (RETURN to quit):\n>>> ")

while line_x != "":
    x = float(line_x)
    y = float(input("Enter Y Coordinate:\n>>> "))
    
    distance = sqrt((new_x - x) ** 2 + (new_y - y) ** 2)
    perimeter = perimeter + distance
    
    new_x = x
    new_y = y
    
    line_x = input("Enter X Coordinate (RETURN to quit):\n>>> ") 

distance = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)

perimeter = perimeter + distance
print("The parimeter of the Polygon is:", perimeter)