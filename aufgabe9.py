import time

def vermeiden(wort, verboten):
    for i in range(len(verboten)):
        if verboten[i] in wort:
            return False
    return True


def verwendet_alle(wort, erforderlich):
    zaehler = 0
    for i in range(len(erforderlich)):
        if erforderlich[i] in wort:
            zaehler = zaehler + 1
            #print(zaehler)
        else:
            return False
    if zaehler == len(erforderlich):
        return True

def verwendet_alle_alternative(wort, erforderlich):
    for i in range(len(erforderlich)):
        if not erforderlich[i] in wort:
            return False
    return True

def ist_palindrom(wort):
    for i in range(len(wort)//2):   #dieses //2 kann man sich sparen
        print(i, wort[i])
        print(i, wort[-i], "\n")
        if wort[i] != wort[-i-1]:
            return False
    return True

wort = "lagerregal"
verboten = "acj"
erforderlich = "alex"
print(vermeiden(wort, verboten))
print(verwendet_alle(wort, erforderlich))
print(ist_palindrom(wort))

#Zusatz
#anf = time.time()
#end = time.time()
#print('{:5.16f}s'.format(end-anf))