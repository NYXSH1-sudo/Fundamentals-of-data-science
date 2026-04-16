marks = []

for i in range(1, 7):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 6
percentage = (total / 600) * 100   # assuming each subject is out of 100

if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

# Output
print("\n----- Result -----")
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Grade:", grade)