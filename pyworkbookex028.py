print("The Wind Chill Calculator\n")

Ta = int(input("Enter tempature in Celsius:\n>>> "))

V = int(input("Enter the wind speed in km/h:\n>>> "))

wind_chill = 13.12 + ((0.6215 * Ta) - (11.37 * V **.16) + (0.3965 * Ta * V **.16))

print("The wind chill is: %.2f" % wind_chill)