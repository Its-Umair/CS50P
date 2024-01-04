email = input("What's your email address? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else:
    print("invalid")