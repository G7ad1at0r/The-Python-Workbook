print("BMI Calculator\n")

height = float(input("Enter height in meters:\n>>> "))
weight = float(input("Enter weight in kg:\n>>> "))

bmi = weight / (height * height)

print("Your BMI is: %.0f" % bmi)
# 18.5 - 24.9 = healthy
# 25 - 29.9 = overweight
# 30+ = obese // -18.5 = under weight
if bmi < 18.5:
    print("You are under weight.")
elif bmi >= 18.5:
    print("You are healthy.")
elif bmi >= 25:
    print("You are over weight.")
elif bmi >= 30:
    print("You are obese.")