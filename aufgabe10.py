def c2f(c):
    return c*1.8+32

l = [0, 20, 30, 50, 80, 100]
l2 = []

for c in l:
    l2.append(c2f(c))

#print(l)
print(l2)