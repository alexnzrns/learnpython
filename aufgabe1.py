# Erste Möglichkeit
eingabe = input("Geben sie die Anzahl an Cent ein: ")
eingabe = int(eingabe)
ausgabe = eingabe / 100
print("Das ergibt ", ausgabe, "Dollar")


# Zweite Möglichkeit
print("Geben Sie einen Betrag in Cent ein: ")
cent = input()
print("Das entspricht", cent[:-2], "Euro und", cent[-2:], "Cent")