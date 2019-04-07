number = int(input("Enter an integer to compute:\n>>> ")) 
print(str(number))

total = 0 

while (number > 0) : 
    digit = number % 10 
    total = total + digit 
    number = number // 10 

print("The total sum of the integer is:",total)