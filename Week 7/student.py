class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Please provide a name")
        if not house:
            raise ValueError("Please provide a house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self.house

    @house.setter
    def house(self, house):
        if house not in ["Barazai", "Hazro", "Musa", "Behbodi"]:
            raise ValueError("Invalid house")
        self.house = house


def main():
    student = get_student()
    student.house = "Mohallah Maghrabi Dhok Barazai"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
