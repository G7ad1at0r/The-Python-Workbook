print("Is That Phrase A Palindrome?\n")

palindrome = input("Enter A Phrase:\n>>> ")
#remove all spaces.
palindrome1 = palindrome.replace(" ", "")
#remove all upper case.
palindrome1 = palindrome1.lower()
#remove all special characters and numbers.
for char in "1234567890@#$_&-+()/?!;:\"'£¢€¥^°={}][✓™®©%~`|•√π÷×¶∆><":
    palindrome1 = palindrome1.replace(char, "")

rev_palindrome = palindrome1[::-1]

answer = False

while palindrome1 != rev_palindrome:
    answer = False
    break
else:
    answer = True

if answer == True:
    print(palindrome1, "is a Palindrome!\n")
else:
    print(palindrome1, "is NOT a Palondrome!\n")

print("Your Original Phrase:", palindrome, "\n")