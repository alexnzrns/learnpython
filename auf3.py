first = float(input("Erste Zahl:"))
second = float(input("Zweite Zahl: "))
operand = input("Operand: ")

if operand == "+":
    erg = first + second
elif operand == "-":
    erg = first - second
elif operand == "*":
    erg = first * second
elif operand == "/":
    erg = first / second

print("Ergebnis", erg)