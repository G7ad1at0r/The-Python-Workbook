print("The Pi Approximator\n")

import math

sum = 3
factor = 2 
sign = 1
i = 1
count = int(input("How many approximations of pi:\n>>> "))

while i < count + 1:
    sum += sign * 4 / (factor * (factor + 1) * (factor + 2))
    error = str(abs(math.pi - sum) * 100) + "%"
    if i <= 9:
        print("{i}  | {sum} ({error})".format(i=i, sum=sum, error=error))
        factor += 2
    else:
        print("{i} | {sum} ({error})".format(i=i, sum=sum, error=error))
        factor += 2        
    if sign is 1:
        sign = -1
    else:
        sign = 1
    i += 1