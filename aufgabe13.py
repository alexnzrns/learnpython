liste = [1, 2, 3, 4, 4, 5, 6, 7, 8]
listeb1 = ['Windsbach', 'Neuendettelsau', 'Nürnberg']
listeb2 = ['Nürnberg', 'Berlin', 'Düsseldorf']
listeb1.extend(listeb2)
palinlist = ['otto', 'lagerregal', 'mensch', 'rentner', 'joschisteinhund']

def summe(liste):
    count = 0
    for i in range(len(liste)):
        count += liste[i]
    return count

def entferne_duplikate(paramliste):     #geht auch mit der set() Funktion für Listen
    newlist = []
    for string in paramliste:
        if string not in newlist:
            newlist.append(string)
    return newlist

def finde_palindrom(paramliste):
    newlist = []
    for string in paramliste:
        if string == string[::-1]:
            newlist.append(string)
    return newlist

def alternativ_finde_palindrom(word):   #bissl komplizierter, oberer Ansatz besser
    for i in range(1, int(len(word)/2)):
        if word[i-1] != word[-i]:
            return 0
    return 1

e1 = summe(liste)
e2 = entferne_duplikate(listeb1)
e3 = finde_palindrom(palinlist)
print("Aufgabe a: Die Summe der ersten Liste ist:", e1)
print("Aufgabe b: Die Liste mit nicht doppelten Einträgen:", e2)
print("Aufgabe c: Liste von Palindromen: ", e3)