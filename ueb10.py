def c2f(liste):
    return liste * 1.8 + 32

celliste = [20, 30, 50, 0, 100]
fliste = []
for i in celliste:
    fliste.append(c2f(i))
print(fliste)

maxwert = max(fliste)
print("Maximaler Wert: ", maxwert)