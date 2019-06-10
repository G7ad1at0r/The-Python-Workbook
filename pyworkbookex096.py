def password_checker(password):
    """Check if a password is good"""
    upper = False
    lower = False
    number = False
    
    for character in password:
        if character >= "A" and character <= "Z":
            upper = True
        elif character >= "a" and character <= "z":
            lower = True
        elif character >= "0" and character <= "9":
            number = True
            
    if len(password) >= 8 and upper and lower and number:
        return True
    else:
        return False
            
def main():
    print("The Password Checker\n")
    
    pwd = input("Enter Your Password:\n>>> ")
   
    password_checker(pwd)
    
    if password_checker(pwd):
        print("Password Is Good")
    else:
        print("Password Is Bad")

if __name__ == "__main__":
    main()