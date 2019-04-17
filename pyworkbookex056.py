print("The Phone Bill Calculator\n")

min = float(input("Enter Minutes Used:\n>>> "))
msg = float(input("Enter Messages Sent:\n>>> "))
data = float(input("Enter Data Used In Gigabytes:\n>>> "))

min_cost = 0
msg_cost = 0
data_cost = 0

if min <= 50:
    min_cost = 0
elif min >50:
    min_cost = (min - 50) * .25
    print("Overage of Minutes Occurred")
    print("$%.2f" % min_cost)

if msg <= 50:
    msg_cost = 0
elif msg > 50:
   msg_cost = (msg - 50) * .15
   print("Overage of Messages Occurred")
   print("$%.2f" % msg_cost)
   
if data <= 1:
    data_cost = 0
elif data >= 1:
    data_cost = (data - 1) * 5
    print("Overage of Data Occurred")
    print("$%.2f" % data_cost)

basic_plan = 15
emerg = .44
pre_total = basic_plan + min_cost + msg_cost + data_cost + emerg
tax = pre_total * .05
grand_total = pre_total + tax

print("Your Total Bill Is: $%.2f" % grand_total)