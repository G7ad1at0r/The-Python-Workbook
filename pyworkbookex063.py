print("Tempature Table of Tens in Celsius to Fahrenheit\n")

print(" Celsius   |   Fahrenheit")
print("==========================")

for temp in range(0, 110, 10):
    fahrenheit = ((temp * 9) / 5) + 32
    if temp == 0:
        fahrenheit = 32
        print(f"     {temp}     =    %2.f         " % fahrenheit)
    elif temp == 100:
        fahrenheit = 212
        print(f"     {temp}   =    %2.f         " % fahrenheit)
    else:
        print(f"     {temp}    =    %2.f         " % fahrenheit)