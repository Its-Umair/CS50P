name = input("What is your name? ")

match name:
    case "Harry" | "Harmione" | "Ron:
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")