print("The Frequencies Of Music")

c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88

name = input("Enter a note(eg. c4):\n>>> ")

note = name[0]
octave = int(name[1])

freq = -1

if note == "c" or note == "C":
    freq = 261.63
elif note  == "d" or note == "D":
    freq = 293.66
elif note == "e" or note == "E":
    freq = 329.63
elif note == "f" or note == "F":
    freq = 349.23
elif note == "g" or note == "G":
    freq = 392.00
elif note == "a" or note == "A":
    freq = 440.00
elif note == "b" or note == "B":
    freq = 493.88

freq /= 2 ** (4 - octave)

print("The frequency of", note.title(), octave, "is %.2f Hz." % freq)