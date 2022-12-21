import re

def isbncheck(param):
    pat = r"\d{3}[- ]\d{1}[- ]\d{5}[- ]\d{1}[- ]"
    if not re.findall(pat, param):
        return False

    return True

print(isbncheck("978-3-86680-192-9"))