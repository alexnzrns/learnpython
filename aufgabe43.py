def verd(daten: list):
    diction = {}
    for i in daten:
        if i not in diction:
            diction[i] = 1
        else:
            diction[i] += 1

    for key in diction:
        print('{}: {}'.format(key, diction[key]))

verd([1, 1, 1, 1, 0, -1, -1, 2, 2, 2, 2, 2, 2])