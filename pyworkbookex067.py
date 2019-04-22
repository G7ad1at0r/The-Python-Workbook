print("Welcome To The Zoo Admission Calculator\n")

age = ()
cost = 0
guests = 0
age_num = 0
age = input("Enter the age of the first guest (RETURN to quit):\n>>> ")

while age != "":
    age_num = int(age)
    guests += 1
    age_num = int(age)
    if age_num <= 2:
        cost = 0 + cost
    elif age_num <= 12:
        cost = 14 + cost
    elif age_num <= 64:
        cost = 23 + cost
    elif age_num >= 65:
        cost = 18 + cost
    age = input("Enter the age of the next guest (RETURN to quit):\n>>> ")
if age == "":
    print(f"Total Cost of {guests} Guests: $%.2f" % cost)