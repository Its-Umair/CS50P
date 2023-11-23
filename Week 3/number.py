def det_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not a integer")
        else:
            break
    return x