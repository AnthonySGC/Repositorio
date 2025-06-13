# Ejercicio 1
def guardar_frases():
    nombre_archivo = input("Ingrese el nombre del archivo (con .txt al final): ")

    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            while True:
                frase = input("Escribe una frase (o escribe 'salir' para terminar): ")
                if frase.lower() == 'salir':
                    break
                archivo.write(frase + '\n')
            print(f"\nLas frases han sido guardadas en '{nombre_archivo}'.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

guardar_frases()
