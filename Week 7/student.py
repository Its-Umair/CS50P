class Student:
    def __init__(self, name, house, passion):
        if not name:
            raise ValueError("Please provide a name")
        if not house:
            raise ValueError("Please provide a house")
        if house not in ["Barazai", "Hazro", "Musa", "Behbodi"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.passion = passion

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.passion:
            case "A"
                return "🧿"
            case "B"
                return "💣"
            case "C"
                return "🔑"
            


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    passion = input("Passion: ")
    return Student(name, house, passion)


if __name__ == "__main__":
    main()
