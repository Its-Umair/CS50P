import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "house": home})
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")