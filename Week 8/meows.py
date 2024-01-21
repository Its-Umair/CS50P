def meow(n: int):
    return "meow\n" * n


number: int = int(input("Number: "))
meows = meow(number)
print(meows, end="")
