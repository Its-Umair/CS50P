import re


name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(1) + " " + matches.group(2)
print(f"hello, {name}")
