import re

string = "Bla Kbla bla 30.2.19 Mai blaK  Maijuni MaiJuni bla 24.12.2022 K Mai"
print(string)

pattern = r"\bMai\b" #raw-String

m1 = re.findall(pattern, string)
print(len(m1))

m2 = re.sub(pattern, "Juni", string)
print("m2:", m2)

m3 = re.sub(r"\bJuni\b", "Monat Juni", m2)
print("m3:", m3)

m4 = re.sub("K", "T", m3)
print("m4:", m4)

pattern = r"[0123]?\d\.[01]?\d\.\d{2,4}"
m5 = re.findall(pattern, string)
print(m5)