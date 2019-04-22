print("~~~~Grade Point Average Calculator~~~~\n")

grade_letter = ()
float_grade = 0
average_count = 0

while grade_letter != "":
    grade_letter = input("Enter A Grade Letter:\n>>> ")
    average_count += 1
  
    if grade_letter == "a+" or grade_letter == "A+":
        float_grade = 4.10 + float_grade
    elif grade_letter == "a" or grade_letter == "A":
        float_grade = 4.0 + float_grade
    elif grade_letter == "a-" or grade_letter == "A-":
        float_grade = 3.70 + float_grade
    elif grade_letter == "b+" or grade_letter == "B+":
        float_grade = 3.50 + float_grade
    elif grade_letter == "b" or grade_letter == "B":
        float_grade = 3.00 + float_grade
    elif grade_letter == "b-" or grade_letter == "B-":
        float_grade = 2.7 + float_grade
    elif grade_letter == "c+" or grade_letter == "C+":
        float_grade = 2.3 + float_grade
    elif grade_letter == "c" or grade_letter == "C":
        float_grade = 2.0 + float_grade
    elif grade_letter == "c-" or grade_letter == "C-":
        float_grade = 1.7 + float_grade
    elif grade_letter == "D+" or grade_letter == "D+":
        float_grade = 1.3 + float_grade
    elif grade_letter == "d" or grade_letter == "D":
        float_grade = 1.0 + float_grade
    elif grade_letter == "f" or grade_letter == "F":
        float_grade = 0 + float_grade
    elif grade_letter == "":
        gpa = float_grade / (average_count - 1)  
        average_counter = average_count - 1

print("The Grade Point Average Is: %.1f" % gpa)
print("Total Grades Calculated: %.1f "% average_counter)