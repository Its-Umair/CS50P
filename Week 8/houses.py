students = [
    {"name": "Umair", "house": "Barazai"},
    {"name": "Ali Aarish", "house": "Yasin"},
    {"name": "Qaseem", "house": "Hazro"},
    {"name": "Basit", "house": "Hazro"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
