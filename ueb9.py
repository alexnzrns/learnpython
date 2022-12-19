def inword(eingabe, verboten):
    for i in range(len(verboten)):
        if verboten[i] in eingabe:
            return False
    return True

def verwendet_alle(wort, zeichen):
    for i in zeichen:
        if i not in wort:
            return False
    return True

def ist_palindrom(wort):
    for i in range(len(wort)): #Länge vom Wort durchiterieren
        if wort[i] != wort[-i-1]:
            return False
    return True

print(inword("Hallo", "a"))
print(verwendet_alle("Alexander", "v"))
print(ist_palindrom("lagerregal"))