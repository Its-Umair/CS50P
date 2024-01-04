email = input("What's your email address? ").strip()

username, domain = email.split("@")

if username:
    print("valid")
else:
    print("invalid")