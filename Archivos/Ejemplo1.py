# Creación de archivos en python

#Declarar un objeto de tipo archivo
archi1=open("datos.txt","w")
archi1.write("Primera linea \n")
archi1.write("Segunda linea \n")
archi1.write("Tercera linea \n")
archi1.close()
print("Final del programa")