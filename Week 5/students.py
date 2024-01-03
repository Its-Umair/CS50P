import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": name, "house": house})
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")