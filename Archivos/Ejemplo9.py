#Solicitando datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido:" )
edad = input("Ingresa tu edad: ")
salario = input("Ingresa tu salario: ")

#Formatear los datos en una línea
linea = f"{nombre},{apellido},{edad},{salario}\n"
#Guardar los datos en un archivo
with open("datos_usuarios.txt", "a") as archivo:
    archivo.write(linea)
print("Datos guardados correctamente en Datos_usuarios.txt")