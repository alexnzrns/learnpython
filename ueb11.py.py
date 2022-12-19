def refrain(text, n):
    for i in range(n):
        print(text)

print(refrain("Jinge bells, jingle bells, jingle all the way", 2))

myfriends = ["Josch", "Pipo", "Lucas", "Stoner"]
print(*myfriends)
eingabe = input("Name eingeben: ")

if eingabe in myfriends:
    myfriends.remove(eingabe)
    print(*myfriends)
else:
    print("Fehlermeldung")