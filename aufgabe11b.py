list = ['Philipp', 'Gabriel', 'Stephan', 'Janis']
print("\nUrsprünglich angelegte Liste:")
for i in list:
    print(i)

name = input("\nName zum löschen eingeben: ")
if name in list:
    list.remove(name)
else:
    print(name, "ist nicht in der Liste enthalten")

print("\nNeue, gelöschte Liste: ")
for i in list:
    print(i)
