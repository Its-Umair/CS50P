class Hat:
    def __init__(self):
        self.houses = ["Barazai", "Hazro", "Attock", "Kamra"]
    def sort(self, name):
        print(name, "is in", "some house")


hat = Hat()
hat.sort("Harry")
