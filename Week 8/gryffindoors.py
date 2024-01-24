students = [
    {"name": "Umair", "house": "Barazai"},
    {"name": "Ali Aarish", "house": "Hazro"},
    {"name": "Qaseem", "house": "Hazro"},
    {"name": "Abdul Basit", "house": "Hazro"},
]

def is_gryffindor(s):
    return s["house"] == "Hazro"


gryffindor = filter(is_gryffind, students)