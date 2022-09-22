def loesche_erstes(list):
    del list[0] # kann man auch mit folgendem machen: >>> list.remove(list[0])
    return list

def ist_sortiert(list):
    for i in range(1, len(list)):
        if list[i-1] > list[i]:
            return False
    return True
        

x = [1, 2, 3, 5, 4]
loesche_erstes(x)
print(x)
print(ist_sortiert(x))