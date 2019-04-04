from fractions import Fraction

print("The Celsius Converter\n")

celsius = float(input("Enter temperature in Celsius:\n>>> "))

print(celsius, "degrees Celsius converts to:\n")

fractions = Fraction(9,5)
fahrenheit = (celsius * Fraction(9,5)) + 32 

print(round(fahrenheit), "degrees fahrenheit\n")

kelvin = celsius + 273.15
print(round(kelvin), "degrees kelvin")