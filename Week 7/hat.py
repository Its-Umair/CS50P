import random


class Hat:
    def __init__(self):
        self.houses = ["Barazai", "Hazro", "Attock", "Kamra"]

    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)


hat = Hat()
hat.sort("Harry")
