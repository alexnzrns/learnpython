def loesche_erstes(mylist: list):
    del mylist[0]
    del mylist[-1]
    return mylist

print(loesche_erstes(["Hallo", "Test", "Zwei", "Drei"]))

def ist_sortiert(mylist):
    for i in range(1, len(mylist)):
        if mylist[i-1] > mylist[i]:
            return False
    return True

print(ist_sortiert([1, 2, 3, 4, 5, 3, 3]))