toonie = 200
loonie = 100
quarter = 25
dime = 10
nickle = 5
pennie = 1

cents = int(input("How many cents?\n>>> "))

print("Your change:\n", cents, " in cents\n")


print(cents // toonie, " toonies")
change = cents % toonie

print(change // loonie, " loonies")
change = cents % loonie

print(change // quarter, " quarters")
change = cents % quarter

print(change // dime, " dimes")
change = change % dime

print(change // nickle, " nickles")
change = change % nickle

print(change, " pennies\n")
change = change % pennie

print(change, " cents remaining")