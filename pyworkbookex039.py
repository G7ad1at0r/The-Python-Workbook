print("Name That Noise\n")

decibel = int(input("Enter the sound level in Decibels:\n>>> "))

if decibel <= 10:
    print("Sorry I did not hear you.")    
elif decibel <= 20:
    print("I don't hear a thing. SHHH!'")
elif decibel <= 40:
    print("It's no louder than a quiet room.")
elif decibel == 70:
    print("Wake up sleepy! It's as loud as a alarm clock.")
elif decibel <= 69:
    print("Noise level is in between a quiet room and a alarm clock.")
elif decibel <= 105:
    print("Noise level is in between a alarm clock and a lawnmower")
elif decibel == 106:
    print("Stay off the grass! Don't you hear the lawnmower'")
elif decibel <= 129:
    print("Noise level is in between a lawnmower and a jackhammer.")  
elif decibel == 130:
    print("Danger Construction Zone\nExcessive noise due to jackhammer.")
elif decibel >= 150:
    print("Cover your ears. Its dangerously loud.\nEar drums rupture at 150 Db.") 
elif decibel >= 200:
    print("Welcome to the big bang.")