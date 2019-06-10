from PyWorkbookEX096 import password_checker
from PyWorkbookEX094 import random_password

def main():
    print("The Random Password Generator\n          \
    &\n       Strenth Checker\n")
    
    count = 0
    pwd = random_password()
    password_checker(pwd)
    
    while password_checker(pwd) == False:
        count += 1        
        password_checker(pwd)
        print(f"Attempt: {count}")
        print(pwd)
        print("Bad Password\n")
        pwd = random_password()
        
    else:
        count += 1
        print(f"Attempt: {count}")
        print(pwd)
        print("Good Password\n")
                        
if __name__ == "__main__":    
    main()