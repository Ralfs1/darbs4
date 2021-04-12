f = open("dati.txt",'w')
saturs = f.write("Šodien ir aprīlis")
f.close()

f = open("dati.txt")
saturs = f.read()
f.close()


print(saturs)