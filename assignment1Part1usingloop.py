# Student Grade Calculator using Loop

# input student's name
name = input("Please enter student name: ")

# input number of subjects
n_s = int(input("Please enter number of subjects: "))

# loop to get marks
total = 0
for i in range(1, n_s + 1):
    marks = float(input(f"Please enter marks for subject {i}: "))
    total += marks

# calculation of average marks
average = total / n_s

# assigning grades
if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

# rendering result
print("\n" + "="*30)
print(f"Student Name: {name}")
print(f"Total Marks: {total:.1f}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print("="*30)