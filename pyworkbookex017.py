water_heat_capasity = 4.186
electricity_price = 8.9
j_to_kwh = 2.777e-7

volume = float(input("Enter the amount of water in milliliters\n>>> "))

d_temp = float(input("Enter the tempature increase (degreese celsius)\n>>> "))

joules = volume * d_temp * water_heat_capasity

print("That will require %.2f Joules of energy." % joules)

kwh = joules * j_to_kwh

cost = kwh * electricity_price

print("The cost of electricity is %.2f cents per hour" % cost)