print("Average Joe's Averages")

exit = False
sum = 0
count = 0
average = 0

while not exit:
    numbers = int(input("Enter Numbers (Enter 0 to EXIT):\n>>> "))
    if numbers > 0:
        count += 1
        sum += numbers
        average = sum / count
    else:
        exit = True
        print("The sum of all numbers is:", sum)
        print("The average of all", count,"numbers is %.2f." % average)
        print("\nGood Bye!")