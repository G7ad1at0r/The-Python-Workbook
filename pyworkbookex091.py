def precedence(string):
    '''Assign a value to a operator'''
    if (string == "+" or string == "-"):
        return 1
    elif string == "*" or string == "/":
        return 2
    elif string == "^":
        return 3
    else:
        return -1
    
if __name__ == "__main__":
   
    print("Smooth Operator Of Precedence")

def main():
    string = input("Enter A Operator:\n>>> ")    
    
    precedence(string)
    
    if precedence(string) > 0:
        print(string, "Is A Operator:",precedence(string))
    elif precedence(string) < 0:
        print(string, "Is NOT A Operator:",precedence(string))
main()