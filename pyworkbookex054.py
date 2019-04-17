print("Wavelenths of Visible Light\n")

nm = float(input("Enter the wavelenth of light in nanometers:\n>>> "))

if nm < 380:
    print("Resonse to low")
    color = "Invalid"
elif nm >= 380 and nm < 450:
        color = "Violet"
elif nm >= 450 and nm < 495:
        color = "Blue"
elif nm >= 495 and nm < 570:
        color = "Green"
elif nm >= 570 and nm < 590:
        color = "Yellow"
elif nm >= 590 and nm < 620:
        color = "Orange"
elif nm >= 620 and nm < 750:
        color = "Red"
else:
    color = "Invalid"
    print("Response to high.")
    

print(nm, "nanometers results in a color of", color)