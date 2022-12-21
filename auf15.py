eingabe = input("eingabe: ")

diction = {}

while eingabe != "":
    if eingabe not in diction:
        diction.update({eingabe: 1})
    elif eingabe in diction:
        diction[eingabe] += 1
    eingabe = input("eingabe: ")

print(diction)