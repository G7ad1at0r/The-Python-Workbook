print("The Seconds Calculator\n")

days = int(input("Enter the amount of Days:\n>>> "))
hours = int(input("Enter the amount of Hours:\n>>> "))
minutes = int(input("Enter the amount of Minutes:\n>>> "))

day_s = days * 86400
hour_s = hours * 3600
minute_s = minutes * 60


seconds = day_s + hour_s + minute_s

print("The total is:\n", seconds, "seconds")