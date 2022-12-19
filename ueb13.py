def makesum(liste):
    summe = 0
    for i in liste:
        summe += liste[i]
    return summe

def entferne_duplikate(liste):
    newlist = []
    for i in liste:
        if i not in newlist:
            newlist.append(i)
    return newlist

def finde_palindrom(liste):
    newlist = []
    for i in liste:
        if i == i[::-1]:
            newlist.append(i)
    return newlist