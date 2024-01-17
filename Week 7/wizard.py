class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        self.subject = subject

    ...
