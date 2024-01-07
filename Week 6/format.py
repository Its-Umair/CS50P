import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(1) + " " + matches.group(2)
print(f"hello, {name}")