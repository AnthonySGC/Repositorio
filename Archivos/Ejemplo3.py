#Leer el contenido del archivo de texto "datos.txt" línea a línea.
archi1=open("datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea, end='')
    linea=archi1.readline()
archi1.close()