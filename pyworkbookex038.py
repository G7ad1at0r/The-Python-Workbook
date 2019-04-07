print("Days in a Month of the Gregorian Calendar\n")

month = str(input("Enter a Month:\n>>> "))

if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    print(month.title(), "has 31 days.")
elif month == "febuary":
    print("Febuary has 28 days.\n29 if it is a leap year.")
elif month == "april" or month == "april" or month == "june" or month == "september" or month == "november":
    print(month.title(), "has 30 days.")
else:
    print("That is not in the Gregorian calendar.")