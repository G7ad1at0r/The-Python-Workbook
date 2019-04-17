print("To Leap or Not To Leap Year\n")

year = int(input("Enter A Year:\n>>> "))

if year % 400 == 0:
    print(year, "is a leap year!")
elif year % 100 == 0:
    print(year, "is not a leap year!")
elif year % 4 == 0:
    print(year, "is a leap year!")
else:
    print(year, "is not a leap year!")