names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
