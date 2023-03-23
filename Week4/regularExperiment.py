import re

s = "ABC123"


if re.match("[A-Z]{3}[0-9]{3}", s):
    print("Matches")
else:
    print("Doesn't match")

