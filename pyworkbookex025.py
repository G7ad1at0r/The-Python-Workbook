print("Seconds to Days Hours Minutes Calculator\n")
# 90,060 = 1 day 1 hour 1 min
seconds = int(input("Enter the amount of seconds:\n>>> "))

days = seconds // 86400
print("Days:", days)

hours = (seconds - (days * 86400)) // 3600
print("Hours:", hours)

minutes = (seconds - ((days * 86400) + (hours * 3600))) // 60
print("Minutes:", minutes)

remaining = seconds - ((days * 86400) + (hours * 3600) + (minutes * 60))
print("Seconds:", remaining)

print("Total: dd:hh:mm:ss\n%02d:%02d:%02d:%02d" % (days, hours, minutes, remaining))