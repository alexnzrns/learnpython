# Erzeugung eines Dictionary
alter = {"Peter":31, "Julia":28, "Werner":35}

print(alter)

# Ersetzen eines Werts
alter["Julia"] = 27

# Ein Element hinzu
alter["Moritz"] = 22

# Ausgabe
print("Julia:",alter["Julia"])
print(alter)


# -- Views --

# Werte
w=alter.values()
print(type(w))
for x in w:
    print(x)

# Keys
k = alter.keys()
print(type(k))
print ("Anzahl Keys:",len(k))
for x in k:
    print(x)

# Items
i = alter.items()
print(type(i))
print("Anzahl Items:",len(i))
for x in i:
      print(x)
if ("Julia",28) in i:
       print ("Julia, 28 ist enthalten")