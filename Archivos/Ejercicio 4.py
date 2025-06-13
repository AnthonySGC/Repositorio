#Ejercicio 4
def leer_ascii():
    try:
        with open("ascii.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("📄 Contenido del archivo 'ascii.txt':\n")
            print(contenido)
    except FileNotFoundError:
        print("❌ El archivo 'ascii.txt' no existe. Ejecuta primero el programa de escritura.")

leer_ascii()
