import math

def main():
    print("         Pythagorean Theorem\nThe Missing Lenth Of A Right Triangle\n")

    a = float(input("Enter Side A:\n>>> "))
    b = float(input("Enter Side B:\n>>> "))

    pythagorean(a, b)
    print("\nThe lenth of the hypotenuse is: %.6f" % pythagorean(a, b))
    
def pythagorean(a, b):
    '''Calculate the hypotenuse of a right triangle'''
    c = math.sqrt((a **2) + (b **2))
    return(c)
    
main()