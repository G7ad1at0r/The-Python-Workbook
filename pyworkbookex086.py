from PyWorkbookEX085 import ordinal

print("The 12 Days Of Christmas\n")

def twelve_days_of_christmas(number):
    print("On the", ordinal(number),"day of Christmas my true love\nsent to me.")
    end = "And a partridge in a pear tree."
    if number == 1:
        print("A partridge in a pear tree.")
    elif number == 2:
        print("Two turtle doves.")
    elif number == 3:
        print("Three french hens.")
    elif number == 4:
        print("Four calling birds.")
    elif number == 5:
        print("Five golden rings.")
    elif number == 6:
        print("Six geese a laying.")
    elif number == 7:
        print("Seven swans a swiming.")
    elif number == 8:
        print("Eight maids a milkings.")
    elif number == 9:
        print("Nine ladies dancing.")
    elif number == 10:
        print("Ten lords a leaping.")
    elif number == 11:
        print("Eleven pipers piping.")
    elif number == 12:
        print("Twelve drummers drumming.\nAnd a partridge in a pear tree.")
    else:
        print("There is only 12 verses in this song!")
        
def main():
    number = 0
    for i in range(0, 12):
        number  += 1
        twelve_days_of_christmas(number)
main()