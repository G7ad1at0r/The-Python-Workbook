print("Under Pressure Calculator\n")
# 0.14503774 kPa = 1 psi
kPa = (float(input("Enter Pressure in kPa:\n>>> ")))

psi = kPa * 0.14503774
print("psi:\n%.4f\n" % psi)

# 7.5006156130264 mm of mercury = 1 kPa
mm = kPa * 7.5006156130264
print("mm of mercury:\n%.4f\n" % mm)

# 1 kPa = 0.0098692316931427 atmospheres
atm = kPa * 0.0098692316931427
print("atmospheres:\n%.4f" % atm)