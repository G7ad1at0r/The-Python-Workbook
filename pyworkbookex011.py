miles = int(input("Enter miles traveled: \n>>> "))

gallons = int(input("Enter gallons of gas used: \n>>> "))

mpg = miles / gallons

print("Your average miles per gallon:\n", mpg)

lpg = (100 * 3.785411784) / (1.609344 * mpg)

print("Your average liters per 100 km:\n", lpg)