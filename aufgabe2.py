eingabe = input("Kilometer Anzahl eingeben: ")
eingabe = float(eingabe) #float falls man Kilometer mit Komma angeben will
if eingabe<0:
    print("Fehler!")
else:
    ausgabe = eingabe / 1.609
    print(eingabe, "entsprechen ", ausgabe, "Meilen")


# Lösung Vatter
km = ""

while 1:
    km = input("Bla")

    if km < 0:
        print("Fehler")
    else:
        break
mi = int(km) / 1.609
print("Das entspricht" + str(mi) + "Meilen")