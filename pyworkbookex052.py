print("Grade Point Converter\n")
grade_point = float(input("Enter a Grade Point Average:\n>>> "))

if grade_point <= 0.00:
    grade = "F" 
elif grade_point <= 0.1:
    grade ="D"
elif grade_point <= 1.3:
    grade = "D+" 
elif grade_point <= 1.7:
    grade = "C-"
elif grade_point <= 2.0:
    grade = "C"
elif grade_point <= 2.3:
    grade = "C+"
elif grade_point <= 2.7:
    grade = "B-"
elif grade_point <= 3.0:
    grade = "B"    
elif grade_point <= 3.5:
    grade = "B+"    
elif grade_point <= 3.7:
    grade = "A-"
elif grade_point <= 4.0:
    grade = "A"
elif grade_point > 4.000000000000009:
    grade = "A+"

print("A", grade_point, "grade point average is equivalent to a grade of:", grade)