print("Employee Evaluation\n")

rating = float(input("Enter the employee rating:\n>>> "))

if rating < 0.4:
    print("Performance Unacceptable")
    print("Your yearly raise is $0.00")
    print("Please report to head office to discuss your future with this corporation.")
elif rating < 0.6:
    print("Performance Acceptable")
    bonus = 2400 * 0.4
    print("Your yearly raise is: %.2f" % bonus)
elif rating >= 0.6:
    print("Performance Meritorious.")
    bonus = 2400 * rating
    print(" Your yearly performance has exceeded our expectations.\nYour yearly raise is: %.2f" % bonus)
else:
    print("Invalid Rating")