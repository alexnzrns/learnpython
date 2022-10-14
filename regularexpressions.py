import re

str = "I said-a hip, hop, the hippppppppppie, the hippie\nTo the hip hip hop-a you don't stop the rock\nIt to the bang-bang boogie, say up jump the boogie\nTo the rhythm of the boogie, the beat"
res = re.sub("h[io]p{1,2}","dub", str) #ab 3 'p' hintereinander wird es nicht mehr geändert
sec = re.split(".*h[io]p{1,2}", str)
print(str)
print("\n")
print(res)
print("\n")
print(sec)