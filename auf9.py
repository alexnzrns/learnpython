def vermeiden(wort, verboten):
    for i in range(len(verboten)):
        if verboten[i] in wort:
            return False
    return True

def verwendet_alle(wort, erforderlich):
    for i in range(len(erforderlich)):
        if erforderlich[i] not in wort:
            return False
    return True

def palindrom(wort):
    for i in range(len(wort)//2):
        if wort[i] != wort[-i-1]:
            return False
    return True

print(vermeiden("hallo", "a"))
print(verwendet_alle("HalliHallo", "aio"))
print(palindrom("lagerregal"))