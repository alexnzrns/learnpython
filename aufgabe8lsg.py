from re import X


def summe(n):
    e = int(n*(n+1)/2) 
    return e

def fak(n):
    f = 1
    for i in range(2, n+1):
        f = f*i
    return f

def quersum(n):
    a = 0
    while 1:
        a = a + n % 10
        n = n // 10
        if n == 0:
            return a

def power(n, y):
    e = n
    for i in range(2, y+1):
        e = e*X
    return e

n = int(input("Bitte geben Sie eine ganze Zahl ein: "))

s = summe(n)
print("Summe:\t\t", s)

f = fak(n)
print("Fakultät:\t", f)

q = quersum(n)
print("Quersumme: \t", q)

y = int(input("Bitte geben sie eine ganze Zahl ein: "))
p = power(n, y)
print("Die ", y, ". Potenz von ", n, " ist: ", p)