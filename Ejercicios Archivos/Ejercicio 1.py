# Lectura de archivos de un texto simple
# Intenta abrir y leer el archivo
try:
    with open("poema.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            print(linea.strip())  # .strip() elimina los saltos de línea extra
except FileNotFoundError:
    print("El archivo 'poema.txt' no se encontró.")
