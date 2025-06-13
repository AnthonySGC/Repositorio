#Ejercicio 3
def añadir_a_archivo():
    nombre_archivo = input("Ingrese el nombre o la ruta del archivo de texto: ")
    print("Escribe las frases que quieras añadir. Escribe 'SALIR' para terminar.")

    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        while True:
            linea = input("➤ Añadir: ")
            if linea.strip().upper() == 'SALIR':
                break
            archivo.write(linea + '\n')
    print("✅ Texto añadido correctamente.")

añadir_a_archivo()
