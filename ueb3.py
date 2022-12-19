first = float(input("1. Zahl: "))
second = float(input("2. Zahl: "))
operand = input("Operand: ")

if operand == "+":
    ergebnis = first + second
elif operand == "-":
    ergebnis = first - second
elif operand == "/":
    ergebnis = first / second
elif operand == "*":
    ergebnis = first * second

print("Ergebnis: ", ergebnis)