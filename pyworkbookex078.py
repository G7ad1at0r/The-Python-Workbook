print("Decimal to Binary Converter\n")

number = int(input("Enter a decimal to convert:\n>>> "))

base = 2
result = ""
q = number

r = q % base
result = str(r) + result
q = q // base

while q > 0:
    r = q % base
    result = str(r) + result
    q = q // base

print("\nThe decimal is:", number)      
print("\nThe binary is:", result)