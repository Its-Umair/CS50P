name = input("what's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()