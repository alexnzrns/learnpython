dict = {}
w = input("Enter a word: ")

while w != "":
    if w not in dict.keys():
        dict.update({w: 1})
    else:
        dict[w] += 1
    w = input("Enter a word: ")

for key, value in dict.items():
    print(key + ":", value)

# ab hier Aufgabe b, ist aber keine gute Aufgabe 

freunde = {"Max": "Mustermann", "Eva": "Mustermann", "Felix": "Mustermann"}

if freunde["Max"] == "Mustermann":
    print("enthalten")

for key in sorted(freunde):
    print(key, freunde[key])