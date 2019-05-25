    
def isInteger(string):
    '''Is a string a intereger or not'''
    string = string.strip()
    
    if (string[0] == "+" or string[0] == "-") and string[1:].isdigit():
        return True
    if string.isdigit():
        return True
    return False
    
def main():
    
    string = input("Enter A String:\n>>> ")
    
    if isInteger(string):
        print("That Is A Integer!")
    else:
        print("That Is NOT A Integer!")

if __name__ == "__main__":
    print("The Integer Inspector\n")
    
    main()