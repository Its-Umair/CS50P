def main():
    name = input("What is your name? ").title()
    hello(name)


def hello(to="world!"):
    print("Hello!", to)

main()
hello()