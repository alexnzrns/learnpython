import re
from datetime import datetime

eingabe = input("Eingabe: ")
print(eingabe.count("Mai "))
replaced_eingabe = eingabe.replace("Mai", "Juni")
print(replaced_eingabe)

replaced2 = replaced_eingabe.replace("Juni", "Monat "+"Juni")
print(replaced2)

replaced_eingabe3 = replaced_eingabe.replace("K", "T")
replaced_eingabe3 = replaced_eingabe.replace("k", "t")
print(replaced_eingabe3)

date_eingabe = input("Geben sie die Nachricht mit einem Datum ein: ")
str2date = datetime.strptime(date_eingabe, '%d/%m/%Y')