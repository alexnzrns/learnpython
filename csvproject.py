import pandas as pd

read_file = pd.read_csv (r'/Users/alexandernazarenus/Documents/GitHub/learnpython/acl2_notfound.csv')
read_file.to_excel(r'/Users/alexandernazarenus/Documents/GitHub/learnpython/acl_excel.xlsx', index=None, header=False)

# hier könnte man der Datei schon eine Variable zuordnen, z.B. file_object = 'acl2_notfound.csv'
with open('acl2_notfound.csv') as file_object:
    for line in file_object:
        print(line)