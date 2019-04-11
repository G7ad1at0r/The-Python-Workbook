print("Name That Holliday")

month = str(input("Enter the month:\n>>> "))
day = int(input("Enter the day:\n>>> "))

if month == "january" and day == 1:
    print(month.title(), day, "st Happy New Years.")
elif month == "july" and day == 1:
    print(month.title(), day, "st Happy Birthday Canada.")
elif month == "december" and day == 25:
    print(month.title(), day,"th Merry Christmas.")
else:
    print("Sorry, there is NO Canadian holliday on", month.title(), day)