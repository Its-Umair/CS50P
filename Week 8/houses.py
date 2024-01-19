students = [
    {"name": "Umair", "house": "Barazai"},
    {"name": "Ali Aarish", "house": "Yasin"},
    {"name": "Qaseem", "house": "Hazro"},
    {"name": "Basit", "house": "Hazro"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])
        
for house in sorted(houses):
    print(house)