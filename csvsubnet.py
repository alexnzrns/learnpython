import pandas as pd
import math
import subprocess

fields = ['ip', 'anzahl']
df = pd.read_csv('acl2_notfound.csv', skipinitialspace=True, usecols=fields, sep=';')
#print(df) 
list = []

az_list = df['anzahl'].to_list()
for n in range(len(az_list)):
    c = az_list[n]
    subnet = 32 - math.log2(c)
    if subnet % 1 != 0:
        list.append("-")
    else:
        df["slash"] = list.append(int(subnet))


#print(list)
df["slash"] = list
print(df)
df.to_csv('new_acl.csv', index=False)

adressen_list = df["ip"].to_list()
whois = []

for n in range(len(adressen_list)):
    a = adressen_list[n]
    whois_output = subprocess.run('whois -h whois.ripe.net -- \'--resource'+ a + '\' | grep netname', 
    shell=True, capture_output=True, check=True)#capturing den befehl für output
    print(whois.stdout.decode()) #decode() damit es als String ausgebenen wird und die \n sonst nicht enthält 
    df["netname"] = list.append(whois_output)

