print("Enter you height in FEET followed by INCHES")

feet_height = int(input("Feet:\n>>> "))

inch_height = int(input("Inches:\n>>> "))

print("Your height is", feet_height, "feet", inch_height, "inches\n")
#  1 inch = 2.54cm // 1 foot = 30.48
feet_cm = feet_height * 30.48
inch_cm = inch_height * 2.54
total_height = feet_cm + inch_cm

print("Your height is", total_height, "cm")