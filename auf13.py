def makesum(mylist):
    summe = 0
    for i in mylist:
        summe += i
    return summe

print(makesum([1,2,3,4,5,6]))

def entferne_duplikate(myliste):
    newlist = []
    for i in myliste:
        if i not in newlist:
            newlist.append(i)
    return newlist

print(entferne_duplikate([1, 2, 2, 2, 2, 3, 4, 5, 6, 6, 7]))

def palindrom(mylist):
    newlist = []
    for i in mylist:
        if i == i[::-1]:
            newlist.append(i)
    return newlist
        
palinlist = ["lagerregal", "opa", "rentner", "mama"]
print(palindrom(palinlist))