def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")
    
def get_name():
    name = input("Name: ")
    return name