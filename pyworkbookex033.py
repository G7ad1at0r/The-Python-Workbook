print("Day Old Bread\n")

purchase = int(input("Enter the amount of loaves for purchase:\n>>> "))

fresh_bread = 3.49 * purchase
print("Regualar Price:\n$ %.2f" % fresh_bread)

old_bread = fresh_bread * .60
print("Discounted Price:\n$ %.2f" % old_bread)

savings = fresh_bread - old_bread

print("Total discount:\n$ %.2f" % savings)