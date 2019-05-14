print("   ~~~~~~~Newton's Method~~~~~~~\n[][][]Square Root Guess-Imater[][][]\n")

n = float(input("Enter A Positive Number:\n>>> "))
x = float(input("Enter You Estimate:\n>>> "))

final = (0.5*(x+(n/x)))
print (final)

for i in range(0,10):
    final = (0.5*(final+(n/final)))
    print (final)