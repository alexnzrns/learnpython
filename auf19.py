import csv


def givedata(year, month):
    with open("Umsatzdaten.csv") as file_object:
        content = csv.reader(file_object, delimiter=';')
        header_row = next(content)
        print(content)
        daten = []
        for i in content:
            daten.append(i)
        print(daten)

    
