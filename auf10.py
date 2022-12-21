def c2f(c):
    return c*1.8+32

b = [20, 30, 40, 50]
f = []
for i in b:
    f.append(c2f(b[i]))
print(f)