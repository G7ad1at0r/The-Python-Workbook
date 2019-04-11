print("The Triangle Detector\n")

side_a = int(input("Enter the lenth of side A of the triangle:\n>>> "))
side_b = int(input("Enter the lenth of side B of the triangle:\n>>> "))
side_c = int(input("Enter the lenth of side C of the triangle:\n>>> "))

if side_a == side_b and side_b == side_c and side_a == side_c:
    print("This triangle is called a Equilateral.")
elif side_a != side_b and side_b != side_c and side_c != side_a:
    print("This triangle is called a Scalene.")
else:
    print("This triangle is called a Isosceles.")