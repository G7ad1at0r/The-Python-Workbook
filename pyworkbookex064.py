print("The Penny-Less Penny Of Pennies Problems\n")

total = 0.00
items = input("Enter Price (RETURN to quit):\n>>> ")

while items != "":
    total = total + float(items)
    items = input("Enter Price (RETURN to quit):\n>>> ")     
# 5 = pennies in a nickel
round = total * 100 % 5
# .05 = sum of a nickel 
if round < 2.50:
    cash = total - round / 100
elif round > 2.50:
    cash = total + .05 - round / 100

print("The Total Payable is: $%.2f" % total)   
print("The Total Cash payment is: $%.2f" % cash)