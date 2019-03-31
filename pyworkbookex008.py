widgets = int(input("How many widgets would you like to purchase: \n>>> "))
gizmos = int(input("How many gimos would you like to purchase: \n>>> "))

print("You have ordered: ", widgets)
print("You have ordered: ", gizmos)

widget_weight = 75 * widgets
gizmos_weight = 112 * gizmos
total_weight = widget_weight + gizmos_weight

print("Your order  will ship promptly  and weights:\n", total_weight, " grams.")