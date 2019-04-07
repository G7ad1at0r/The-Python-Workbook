print("The Tripple Integer Sorter\n")

integer1 = int(input("Enter the first integer:\n>>> "))
integer2 = int(input("Enter the second integer:\n>>> "))
integer3 = int(input("Enter the third integer:\n>>> "))

min_integer = min(integer1, integer2, integer3)
print("The lowest integer value is:\n", min_integer)

max_integer = max(integer1, integer2, integer3)
print("The highest integer value is:\n", max_integer)

mid_integer = (integer1 + integer2 + integer3) - (max_integer + min_integer)
print("The middle integer is:\n", mid_integer)

print("The order the integers were entered:\n", integer1, integer2, integer3)

print("The integers in sorted order from max to min value:\n", max_integer, mid_integer, min_integer)

print("The integers in sorted order from min to max value:\n", min_integer, mid_integer, max_integer)