import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")