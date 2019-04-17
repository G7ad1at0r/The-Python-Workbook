print("The Next Day aka Tomorrow\n")

year = int(input("Enter The Year:\n>>> "))
month = int(input("Enter The Month:\n>>> "))
day = int(input("Enter The Day:\n>>> "))

print("\nIf today is {}-{}-{}.".format(year, month, day))

t_year = year
t_month = month
t_day = day
# new years 
if month == 12:
    if day > 30:
        t_year = year + 1
        t_day = 1
        t_month = 1
    elif day < 31:
        t_day = day + 1
# 30 days
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day < 30:
        t_day = 1 + day
    elif day >= 30:
        t_month = month + 1
        t_day = 1
  # 31 days       
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if day <= 30:
        t_day = day + 1
    elif day > 30:
        t_day = 1
        t_month = month + 1
# dealing with Febuary
elif month == 2:
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False        
    if leap == False and day >= 28:
        t_month = month + 1
        t_day = 1
    elif leap == True and day >= 29:
        t_month = month + 1
        t_day = 1
    else:
        t_day = day + 1
  
print("\nThen tomorrow is {}-{}-{}.".format(t_year, t_month, t_day))