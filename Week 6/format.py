name = input("What's your name? ").strip()
if "," in name:
    first, last = name.split(", ")
    name = (f"{first} {last}")
print(f"hello, {name}")