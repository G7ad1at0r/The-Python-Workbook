import math

print("The Quadratic Function\n")

a = int(input("Enter Integer A: "))
b = int(input("Enter Integer B: "))
c = int(input("Enter Integer C: "))

d = b **2 - 4 * a * c 

if d < 0:
    print ("This equation has no solution")
elif d == 0:
    x = (- b + math.sqrt(b **2 - 4 * a * c)) / 2 * a
    print ("This equation has only one solution: "), x
else:
    x1 = (- b + math.sqrt((b **2) - (4 * (a * c)))) / (2 * a)
    x2 = (- b - math.sqrt((b **2) - (4 * (a * c)))) / (2 * a)
    print ("This equation has two solutions: ", x1, " or", x2)