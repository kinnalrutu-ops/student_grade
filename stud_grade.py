import sys
if len(sys.argv) != 6:
    print("Please pass 5 subject marks as command-line arguments!")
    sys.exit()

a = (sys.argv[1])
b = (sys.argv[2])
c = (sys.argv[3])
d = (sys.argv[4])
e = (sys.argv[5])

marks = [a, b, c, d, e]

if any(m < 35 for m in marks):
    grade = "F"
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
