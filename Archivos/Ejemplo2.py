#Lectura de un archivo de texto
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()