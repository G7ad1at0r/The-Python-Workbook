print("The 7 Categories Of Radiation\n")

hz = float(input("Enter The Radiation Frequency In Hz:\n>>> "))
type = ""

if hz <= 3 * 10 **9:
    type = "Radio Waves"
elif hz <= 3 * 10 **12:
    type = "Microwaves"
elif hz <= 4.3 * 10 **14:
    type = "Infrared Light"
elif hz <= 7.5 * 10 **14:
    type = "Visible Light"
elif hz <= 3 * 10 **17:
    type = "Ultraviolet Light"
elif hz <= 3 * 10 **19:
    type = "X-Rays"
elif hz > 3 * 10 **19:
    type = "Gamma Rays"

print("Radiation With", hz,"Hz Is Categorized As:", type)