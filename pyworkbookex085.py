def ordinal(number):
    """Display the ordinal number"""
    if number < 1:
        return("   ")
    elif number == 1:
        return(f"{number}st")
    elif number == 2:
        return(f"{number}nd")
    elif number == 3:
        return(f"{number}rd")
    elif number <= 20:
        return(f"{number}th")
    else:
        return("   ")

if __name__ == "__main__":
    print("Ordinal Numbers\n")
    
    number = int(input("Enter A Number Between 1 - 20:\n>>> "))

    print("\n" + ordinal(number))