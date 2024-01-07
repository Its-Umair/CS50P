import re


name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    first = matches.group(1)
    last = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")