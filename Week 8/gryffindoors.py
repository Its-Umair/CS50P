students = [
    {"name": "Umair", "house": "Barazai"},
    {"name": "Ali Aarish", "house": "Hazro"},
    {"name": "Qaseem", "house": "Hazro"},
    {"name": "Abdul Basit", "house": "Hazro"},
]


def is_gryffindor(s):
    return s["house"] == "Hazro"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
