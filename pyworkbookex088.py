def triangle(a, b, c):
    '''Can three lenths make a triangle'''
    if a >= b + c:
        triangle = False
    elif b >= a + c:
        triangle = False
    elif c >= b + a:
        triangle = False        
    else:
        triangle = True
    
    if triangle == False:
        print("That Is NOT A Triangle!")   
    elif triangle == True:
        print("That Is A Triangle!")
        
if __name__ == "__main__":
    print("IS THAT A TRIANGLE?\n")
    
    a = float(input("Enter side A:\n>>> "))
    b = float(input("Enter side B:\n>>> "))
    c = float(input("Enter side C:\n>>> "))
    
    triangle(a, b, c)