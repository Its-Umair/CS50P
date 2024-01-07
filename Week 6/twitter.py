import re

url = input("URL: ").strip()

re.search(r"^https?://(www\.)?twitter\.com/.+$", url, re.IGNORECASE)