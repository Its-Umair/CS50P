import re

email = input("What's your email address? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid email address")
else:
    print("Invalid email address")
