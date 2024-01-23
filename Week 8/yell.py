def main():
    yell("THIS", "IS", "CS50")


def yell(*words):
    uppercase = [word.upper() for word in words]
    print(*uppercase)


if __name__ == "__main__":
    main()
