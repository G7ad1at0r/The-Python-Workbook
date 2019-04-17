print("License Plate Classifier\n")

plate = input("Enter Your Plate: (ABC123  // 1234ABC)\n>>> ")

if len(plate) == 6:
    if plate[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and plate[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and plate[2] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 
        if plate[3] in "0123456789" and plate[4] in "0123456789" and plate[5] in "0123456789":
            print("Classified as: OLD")
            print("This is a valid plate.")

elif len(plate) == 7:
    if plate[4] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"and plate[5] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and plate[6] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if plate[0] in "0123456789" and plate[1] in "0123456789" and plate[2] in "0123456789" and plate[3] in "0123456789":
            print("Classified as: NEW")
            print("This is a valid plate.")
else:
    print("Plate Invalid")