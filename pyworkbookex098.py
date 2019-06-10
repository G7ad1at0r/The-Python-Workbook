def hex2int(n):
    """Convert Hexadecimal To Integer"""
    n = int(n, 16)
    print(n)
    
def int2hex(n):
    """Convert Integer To Hexadecimal"""
    n = hex(n)
    print(n)


def main():
    print("The Hexadecimal Decimal Digits Converter\n")
    print("1. Hexadecimal to Integer\n2. Integer to Hexadecimal\n")
    
    choice = int(input("Enter Your Choice (0 to quit):\n>>> "))
    
    if choice == 1:
        n = input("Enter A Hexadecimal:\n>>> ")
        hex2int(n)
        
    elif choice == 2:
        n = int(input("Enter A Integer:\n>>> "))
        int2hex(n)
   
    elif choice == 0:
        print("BYE")
   
    else:
        print("Sorry That Is Not A Option")

if __name__ == "__main__":
    main()