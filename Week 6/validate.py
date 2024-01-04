email = input("What's your email address? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")