def s2hms(sec):
    h = sec // 360
    m = (sec // 60)%60
    s = sec % 60
    return h,m,s

def maketupel(liste):
    tup1 = tuple #kann man sich sparen
    tup2 = tuple #kann man sich sparen
    tup1 = liste[0]
    tup2 = liste[-1]
    return tup1, tup2
print(s2hms(989898))
print(maketupel(["Hallo", "Test", "Servus", "Moin"]))
