def main():
    yell(["THIS", "IS", "CS50"])


def yell(words):
    uppercase = []
    for word in words:
        uppercase.append(word.upper())
    print(uppercase)


if __name__ == "__main__":
    main()
