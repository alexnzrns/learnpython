def refrain(text, n):
    for i in range(n):
        print(text)
    
print(refrain("Jinge Jinge", 3))

friends = ["Josch", "Pipo", "Stoner", "Gabriel"]
for i in friends:
    print(i)
name = input("Name eingeben: ")
if name not in friends:
    print("Fehler")
else:
    friends.remove(name)
    print(friends)