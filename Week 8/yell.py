def main():
    yell("THIS", "IS", "CS50")


def yell(*words):
    uppercase = map(str.upper)
    print(*uppercase)


if __name__ == "__main__":
    main()
