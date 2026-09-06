
# First problem : Student Grade Calculator

# Receiving input
name = input("Please enter student's name: ")
subject1 = float(input("Please enter marks for subject 1: "))
subject2 = float(input("Please enter marks for subject 2: "))
subject3 = float(input("Please enter marks for subject 3: "))

# Determining total and average marks
total = subject1 + subject2 + subject3
average = total / 3

# Assigning grades
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

# Rendering result
print(f"\nStudent Name: {name}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")