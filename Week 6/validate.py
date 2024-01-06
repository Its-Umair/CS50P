import re

email = input("What's your email address? ").strip()

if re.search(r"^\w+@\w+\.\w+\.edu$", email, re.IGNORECASE):
    print("Valid email address")
else:
    print("Invalid email address")
