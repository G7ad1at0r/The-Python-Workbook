print("Richter Scale\n")

magnitude = float(input("Enter Magnitude:\n>>> "))

if magnitude <= 2:
    devistation = "Micro"
elif magnitude <= 3:
    devistation = "Very Minor"
elif magnitude <= 4:
    devistation = "Minor"
elif magnitude <= 5:
    devistation = "Light"
elif magnitude <= 6:
    devistation = "Moderate"
elif magnitude <= 7:
    devistation = "Strong"
elif magnitude <= 8:
    devistation = "Major"   
elif magnitude <= 10:
    devistation  = "Great"
elif magnitude > 10:
    devistation = "Holly $&#+ Your Pants Your Disintegrated into Smithereens Type Of"    

print("A", magnitude,"magnitude earthquake is capable of", devistation,"destruction.")