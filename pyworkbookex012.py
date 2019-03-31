import math

start = input("Starting point:\n>>> ")
# Schreiber / 48.809961 / -87.267758
t1 = float(input("Enter longitude of  " + start + ":\n>>> "))

g1 = float(input("Enter latitude of " + start + ":\n>>> "))

print(start, "'s longitude is:\n", t1, "\n", start, "'s latitude is:\n", g1)

end = input("End point:\n>>> ")
# Toronto / 43.653226 / -79.38318429999998
t2 = float(input("Enter longitude of " + end + ":\n>>> "))

g2 = float(input("Enter longitude of " + end + ":\n>>> "))

print(end, "'s longitude is:\n", t2, "\n", end, "'s latitude is:\n", g2)

t1 = math.radians(t1)
g1 = math.radians(g1)

t2 = math.radians(t2)
g2 = math.radians(g2)

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
# 833.72
print("The distance between ", start," and ", end, " is:\n", distance, " KM")
print("The earths radius is 6371.01 KM")