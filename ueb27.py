import re

text = input("Eingabe: ")
pattern = [
    "Michael",
    r"^Michael",
    r"Michael$",
    r"[Mm]ichael",
    r"[\t| ]+",
    r"[a-z0-9><_]",
    r"[\d|+-]",
    r"[^a-zA-Z]",
    r"ab?c",
    r"[aeiou]da",
    r"[a-zA-z]da",
    r"^$",
    r".{3}"
] 

for i in pattern:
    print(re.match(text, i))