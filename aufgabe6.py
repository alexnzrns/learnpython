x = []

while 1:
    y = input("Eingabe:")
    if(y == "stop"):
        break
    x.append(y)

print(x)

#Zusatz um die Liste als "normalen" Text aufzugeben

for wort in x:
    print(wort, end=' ')