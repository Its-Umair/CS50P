class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Please provide a name")
        if not house:
            raise ValueError("Please provide a house")
        if house not in ["Barazai", "Hazro", "Musa", "Behbodi"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return "a student"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
