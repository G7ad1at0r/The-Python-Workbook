print("The Prime Factorization\n")

number = int(input("Enter a number greater than 2:\n>>> "))
number1 = number
factors = []
d = 2

while d * d <= number:
    while (number % d) == 0:
        factors.append(d)
        print(d)
        number //= d
    d += 1

if number > 1:
   factors.append(number)
   print(number)
   
print()
print(str(factors).strip("[]"), f"are the factors of {number1}.")