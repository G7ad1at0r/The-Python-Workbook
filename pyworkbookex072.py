print("Is That Word A Palindrome?\n")

palindrome = input("Enter A Word:\n>>> ")
rev_palindrome = palindrome[::-1]

answer = False

while palindrome != rev_palindrome:
    answer = False
    break
else:
    answer = True

if answer == True:
    print(palindrome, "is a Palindrome!")
else:
    print(palindrome, "is NOT a Palondrome!")