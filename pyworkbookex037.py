print("Whats With That Shape\n")

sides = int(input("How many sides does your shape have?\n>>> "))

if sides <= 2:
    print("No such shape found.\nSorry Please Try Again!!")
elif sides == 3:
    print("Your three sided shape is a TRIANGLE")
elif sides == 4:
    print("Your four sided shape is a SQUARE")
elif sides == 5:
    print("Your five sided shape is a PENTAGON")
elif sides == 6:
    print("Your six sided shape is a HEXAGON")
elif sides == 7:
    print("Your seven sided shape is a HEPTAGON")
elif sides == 8:
    print("Your eight sided shape is a OCTAGON")
elif sides == 9:
    print("Your nine sided shape is a NONAGON")
elif sides == 10:
    print("Your ten sided shape is a DECAGON")    
else:
    print("A POLYGON can have an infinite number of sides.")