month = input("Enter Your Birth Month:\n>>> ")
day = int(input("Enter The Number Of Your Birthday:\n>>> "))

if month == "january":
    if day <= 19:
        sign = "Capricorn"
    else:
        sign = "Aquarius"
elif month == "febuary":
    if day <= 18:
        sign = "Aquarius"
    else:
        sign = "Pisces"
elif month == "march":
    if day <=20:
        sign = "Pisces"
    else:
        sign = "Aries"
elif month == "april":
    if day <= 19:
        sign = "Aries"
    else:
        sign = "Tauris"
elif month == "may":
    if day <= 20:
        sign = "Tauris"
    else:
        sign = "Gemini"
elif month == "june":
    if day <= 20:
        sign = "Gemini"
    else:
        sign = "Cancer"
elif month == "july":
    if day <= 22:
        sign = "Cancer"
    else:
        sign = "Leo"
elif month == "august":
    if day <= 22:
        sign = "Leo"
    else:
        sign = "Virgo"
elif month == "september":
    if day <= 22:
        sign = "Virgo"
    else:
        sign = "Libra"
elif month == "october":
    if day <= 22:
        sign = "Libra"
    else:
        sign = "Scorpio"
elif month == "november":
    if day <= 21:
        sign = "Scorpio"
    else:
        sign = "Sagitarius"
elif month == "december":
    if day <= 21:
        sign = "Sagitarius"
    else:
        sign = "Capricorn"
else:
    sign = "Invalid"
    print("Response Invalid")

print("Your Astrological Sign Is:\n", sign)
print("Your Birthday Is", month.title(), day)