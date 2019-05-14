print("The Maximum Integer Inspector\n")

from random import randrange

max = randrange(1, 101)

print(f"The maximum integer is: {max}")

updates = 0

for i in range(1, 100):
    random = randrange(1, 101)

    if random > max:
        max = random
        updates += 1
        print(random, "<== Update")
    else:
        print(random)
        
print("\nThe maximum value is:", max)
print ("\nTimes the maximum value was found:", updates)