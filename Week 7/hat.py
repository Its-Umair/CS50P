import random


class Hat:
    houses = ["Barazai", "Hazro", "Attock", "Kamra"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
