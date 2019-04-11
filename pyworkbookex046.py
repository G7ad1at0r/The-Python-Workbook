print("The Seasons\n")

month = input("Enter the month:\n>>> ")
day = int(input("Enter the day:\n>>> "))

if month == "january" or month == "febuary":
    season = "Winter"
elif month == "march":
    if day <= 20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "april" or month == "may":
    season = "Spring"
elif month == "june":
    if day <= 20:
        season = "Spring"
    else:
        season = "Summer"
elif month == "july" or month == "august":
    season = "Summer"
elif month == "september":
    if day <= 20:
        season = "Summer"
    else:
        season = "Fall"
elif month == "october" or month == "november":
    season = "Fall"
elif month == "december":
    if day <= 20:
        season = "Fall"
    else:
        season = "Winter"
else:
    print("Response Invalid")
    season = "Invalid"


print("For the date:", month.title(), day)        
print("The season is:", season)