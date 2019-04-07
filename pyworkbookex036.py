print("Vowel or Consonant")

letter = input("Enter a letter:\n>>> ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter", letter.title(), "is a Vowel.")
elif letter == "y":
    print("The letter", letter.title(), "is sometimes a Vowel or Consonant.")
else:
    print("The letter", letter.title(), "is a Consonant.")