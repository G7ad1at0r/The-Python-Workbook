print("The Multiplication Table\n")

max = int(input("Enter the max multiplier:\n>>> "))

print("    ", end="")
for number in range(1, max + 1):      
    print("%4d" % number, end="")
print()    

for number in range(1, max + 1):
    print("%4d" % number, end="")   
    for digit in range(1, max + 1):
        print("%4d" % (number * digit), end="")
    print()