print("Moles Calculator\n")

# 20684271.84 Pascals = 3000 psi
P = float(input("Enter the pressure in Pascals:\n>>> "))

# 12 Liters
V = float(input("Enter the volume in Liters:\n>>> ")) 

# 20 Celsius
T = float(input("Enter the tempature in Celsius:\n>>> "))

# Gas Constant
R = 8.314

# Kelvin 
K = T + 273.15

# PV = nRT
moles = (P * V) / (R * K)

print("The amount of gas in moles is %.3f :" % moles)
# STP = standard tempature 0 C, Pressure 101.325 Paskals