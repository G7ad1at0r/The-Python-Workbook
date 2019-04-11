print("Black or White.\nWhat Color Is The Square\n")

square = input("Enter the coordinates of the square:\n>>> ")

letter = square[0]
number = int(square[1])

if letter == "a" or letter =="c" or letter == "e" or letter == "g":
    if number % 2 == 0:
        color = "White"
    else:
        color = "Black"

elif letter == "b" or letter == "d" or letter == "f" or letter == "h":
    if number % 2 == 0:
        color = "Black"  
    else:
        color = "White"
else:
    print("Invalid")
    color = "Invalid"        

print("Your square is", color)