print("What Note Is That Frequency ?")

freq = float(input("Enter a frequency:\n>>> "))

if freq < 260.62:
    print("Frequency is out of range.")
elif freq >= 260.63 and freq <= 262.63:
    print("The note C4 has a frequency of 261.63 Hz.")
elif freq >= 292.66 and freq <= 294.66:
    print("The note D4 has a frequency of 293.66 Hz.")
elif freq >= 328.63 and freq <= 330.63:
    print("The note E4 has a frequency of 329.63 Hz.")
elif freq >= 348.23 and freq <= 350.23:
    print("The note F4 has a frequency of 349.23 Hz.")
elif freq >= 391.00 and freq <= 393.00:
    print("The note G4 has a frequency of 392.00 Hz ")
elif freq >= 439.00 and freq <= 441.00:
    print("The note A4 has a frequency of 440.00 Hz.")
elif freq >= 492.88 and freq <= 494.88:
    print("The note B4 has a frequency of 493.88 Hz.")
elif freq > 494.89:
    print("The frequency is out of range.")