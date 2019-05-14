print("Binary To Decimal\n")

binary = input("Enter Binary To Be Converted:\n>>> ")

n = len(binary)
result = 0
   
for i in range(1, n + 1):
    result = result + int(binary[i - 1]) * 2 **(n - i)

print("\nThe Binary Is: ", binary)
print ("\nThe Decimal Is:", result)