print("Dog Years\n")

age = float(input("How old is your dog:\n >>> "))


if age <= 0:
    print("Enter a positive integer.")
elif age <= 2:
    age = age * 10.5
    print("Your dog is", age, " years old in human years.")
elif age >= 2:
    age = ((age - 2) * 7) + 21
    print("Your dog is", age, "years old in human years.")