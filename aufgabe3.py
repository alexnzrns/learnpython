zahl1 = input("Geben Sie die 1. Zahl an: ")
zahl1 = int(zahl1)
zahl2 = input("Geben Sie die 2. Zahl an: ")
zahl2 = int(zahl2)

operand = input("Geben Sie den Operand an: ")

if operand == "+":
    ausgabe = zahl1 + zahl2
elif operand == "-":
    ausgabe = zahl1 - zahl2
elif operand == "/":
    ausgabe = zahl1 / zahl2
elif operand == "*":
    ausgabe = zahl1 * zahl2
elif operand == "%":
    ausgabe = zahl1 % zahl2

print(ausgabe)


# Lösung Vatter  -> try and except lernen/verstehen für Fehlerbehebungen

while 1:

    a = input("Bitte gbeen Sie Zahl 1 ein: ")

    try:
        a = int(a)
    except:
        try:
            a = float(a)
        except:
            print("Zahl 1 ungültig!")

while 1:

    b = input("Bitte gbeen Sie Zahl 2 ein: ")

    try:
        b = int(b)
    except:
        try:
            b = float(b)
        except:
            print("Zahl 2 ungültig!")


while 1:

    o = input("Bitte geben Sie einen Operanden (+, -, *, /) ein:")

    if o == "+":
        e = a+b
        break
    elif o =="-":
        e = a-b
        break
    elif o == "*":
        e = a*b
        break
    elif o == "/":
        e = a/b
        break
    else:
        print("Der Operand ist ungültig.\n")

print(e)