meal_cost = float(input("Total before taxes? \n >>> "))

tip = .18 * meal_cost

tax = .14 * meal_cost

total = meal_cost + tip + tax

print("Meal Totoal Before Tax: \n$ %.2f" % meal_cost)

print("Total Tax: \n$ %.2f" % tax)

print("Total Tip: \n$ %.2f" % tip)

print("Your grand total after tax and tip: \n$ %.2f" % total)