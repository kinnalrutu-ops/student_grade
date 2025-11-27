import sys

# If 5 arguments are passed from command line
if len(sys.argv) == 6:
    script_name = sys.argv[0]
    marks1 = int(sys.argv[1])
    marks2 = int(sys.argv[2])
    marks3 = int(sys.argv[3])
    marks4 = int(sys.argv[4])
    marks5 = int(sys.argv[5])
else:
    # Default values
    script_name = sys.argv[0]
    marks1 = 80
    marks2 = 90
    marks3 = 89
    marks4 = 67
    marks5 = 56

marks = [marks1, marks2, marks3, marks4, marks5]

# Fail condition
if any(m < 35 for m in marks):
    grade = "F"
    total = sum(marks)
    percentage = total / 5
else:
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
