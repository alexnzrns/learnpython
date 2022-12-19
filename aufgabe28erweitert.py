with open('aufgabe28.txt') as file:
    contents = file.read()
    print(contents)
    newlist = contents.split('\n')
    list2 = []
    list3 = []
    for i in range(len(newlist)):
        list2.append(newlist[i].replace(".", ""))
    print(list2)
    for i in range(len(list2)):
        list3.append(list2[i].replace(",", "."))
    print(list3)
    erg = 0
    for i in range(len(list3)):
        erg += float(list3[i])
    print(erg)
    #for i in range(len(list2)):