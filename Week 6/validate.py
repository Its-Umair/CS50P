import re

email = input("What's your email address? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid email address")
else:
    print("Invalid email address")