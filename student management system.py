print("Welcome to the student management system program!")
print("Description: ")
print("This program is built to display report card of 2 students.")
print()
students = []
name1 = input("Enter First Student Name: ")
age = int(input("Enter The Age: "))
print()

science_marks = int(input("Enter science marks: "))
maths_marks = int(input("Enter maths marks: "))
geography_marks = int(input("Enter geography marks: "))
print()
name2 = input("Enter second Student Name: ")
age2 = int(input("Enter The Age: "))
print()
science_marks2 = int(input("Enter science marks: "))
maths_marks2 = int(input("Enter maths marks: "))
geography_marks2 = int(input("Enter geography marks: "))
print()
student_1 = {
    "Name":name1,
    "Age": age,
    "Marks": [science_marks,maths_marks,geography_marks]
}
student_2 = {
    "Name":name2,
    "Age": age2,
    "Marks": [science_marks2,maths_marks2,geography_marks2]
}
students.append(student_1)
students.append(student_2)

marks1 = student_1["Marks"]
marks2 = student_2["Marks"]

total_marks1 = sum(marks1)
total_marks2 = sum(marks2)

avg_marks1 = total_marks1 / len(marks1)
avg_marks2 = total_marks2 / len(marks2)

highest1 = max(marks1)
highest2 = max(marks2)

lowest_marks1 = min(marks1)
lowest_marks2 = min(marks2)

if avg_marks1 <= 100 and avg_marks1 >= 90:
    grade1 = "A+"
elif avg_marks1 < 90 and avg_marks1 >= 85:
    grade1 = "A"
elif avg_marks1 < 85 and avg_marks1 >= 75:
    grade1 = "B"
elif avg_marks1 < 75 and avg_marks1 >= 65:
    grade1 = "C"
elif avg_marks1 < 65 and avg_marks1 >= 55:
    grade1 = "D"
else:
    grade1 = "F"

if avg_marks2 <= 100 and avg_marks2 >= 90:
    grade2 = "A+"
elif avg_marks2 < 90 and avg_marks2 >= 85:
    grade2 = "A"
elif avg_marks2 < 85 and avg_marks2 >= 75:
    grade2 = "B"
elif avg_marks2 < 75 and avg_marks2 >= 65:
    grade2 = "C"
elif avg_marks2 < 65 and avg_marks2 >= 55:
    grade2 = "D"
else:
    grade2 = "F"
print("-------STUDENTS REPORT CARD-------")
print()
print(f"Name: {student_1['Name']}")
print(f"Age: {student_1['Age']}")
print(f"Marks: {student_1['Marks']}")
print(f"Highest marks obtained: {highest1}")

print(f"Lowest marks obtained: {lowest_marks1}")
print(f"Average marks obtained: {avg_marks1:.1f}")
print(f"Total marks obtained: {total_marks1}")

print()
print(f"Overall grade: {grade1}")
print()
print(f"Name: {student_2['Name']}")
print(f"Age: {student_2['Age']}")
print(f"Marks: {student_2['Marks']}")

print(f"Highest marks obtained: {highest2}")
print(f"Lowest marks obtained: {lowest_marks2}")
print(f"Average marks obtained: {avg_marks2:.1f}")

print(f"Total marks obtained: {total_marks2}")
print()
print(f"Overall grade: {grade2}")
print()
print("Thank you for using the program!")
print("Goodbye.")