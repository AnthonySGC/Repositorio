#Ejercicio 2
def leer_archivo():
    nombre_archivo = input("Ingrese el nombre o la ruta del archivo de texto: ")
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error: {e}")

leer_archivo()
