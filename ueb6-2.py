mylist = []
while 1:
    eingabe = input("Eingabe: ")
    if eingabe != "Stop":
        mylist.append(eingabe)
    else:
        break
print(*mylist)