students = [
    {"name": "Umair", "house": "Barazai"},
    {"name": "Ali Aarish", "house": "Hazro"},
    {"name": "Qaseem", "house": "Hazro"},
    {"name": "Abdul Basit", "house": "Hazro"},
]

gryffindors = [student["name"] for student in students if student["house"] == "Hazro"]



for gryffindor in sorted(gryffindors):
    print(gryffindor)