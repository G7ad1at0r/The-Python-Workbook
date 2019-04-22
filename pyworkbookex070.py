print("~~Ceasar Cipher~~\nEncoder and Decoder\n")

message = input("Enter a message to encode:\n>>> ")
shifter = int(input("Enter the amount to shift:\n>>> "))
code = ""

for letter in message:
    if letter >= "a" and letter <= "z":
        pos = ord(letter) - ord("a")
        pos = (pos + shifter) % 26
        new_letter = chr(pos + ord("a"))
        code = code + new_letter
    
    elif letter >= "A" and letter <= "Z":
        pos = ord(letter) - ord("A")
        pos = (pos + shifter) % 26
        new_letter = chr(pos + ord("A"))
        code = code + new_letter
        
    else:
        code = code + letter

print("The message is:\n", code)