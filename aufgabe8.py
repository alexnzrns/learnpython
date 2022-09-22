def summe(x):
    
    a = 0
    b = 0

    for i in range(x):
        a = x - i
        b = b + a
            
    return b

endwert = int(input("Geben Sie die Zahl an, bis zu der die Summe berechnet werden soll: "))
print(summe(endwert))