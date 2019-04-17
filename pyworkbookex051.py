print("Letter To Grade Point\n")

grade = input("Enter Your Grade:\n>>> ")
grade_point =0

if grade == "F" or grade == "f":
    grade_point = 0
elif grade == "D" or grade == "d":
    grade_point = 1.0
elif grade == "D+" or grade == "d+":
    grade_point = 1.3
elif grade == "C-" or grade == "c-":
    grade_point = 1.7
elif grade == "C" or grade == "c":
    grade_point = 2.0
elif grade == "C+" or grade == "c+":
    grade_point = 2.3
elif grade == "B-" or grade == "b-":
    grade_point = 2.7
elif grade == "B" or grade == "b":
    grade_point = 3.0
elif grade == "B+" or grade == "b+":
    grade_point = 3.5
elif grade == "A-" or grade == "a-":
    grade_point = 3.7
elif grade == "A" or grade == "a":
    grade_point = 4.0
elif grade == "A+" or grade == "a+":
    grade_point = 4.1
else:
    print("Sorry that grade is invalid.")
    grade_point = "XX.XX"

print("For the grade", grade.title(), "the grade point is", grade_point)