with open("aufgabe28.txt") as file:
    contents = file.read()
    print(contents)
    print(type(contents))
    newlist = contents.split('\n')
    erg = 0
    for i in range(len(newlist)):
        erg += float(newlist[i])
    print(erg)