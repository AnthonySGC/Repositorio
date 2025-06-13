#Ejercicio 2 Contador de Líneas
# Paso 1: Solicitar el nombre del archivo
nombre_archivo = input("📄 Ingresa el nombre del archivo (ej: poema.txt): ")

# Paso 2: Manejo de errores con try...except
try:
    # Paso 3: Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        # Paso 4: Leer todas las líneas
        lineas = archivo.readlines()

        # Paso 5: Contar y mostrar el número de líneas
        cantidad = len(lineas)
        print(f"✅ El archivo contiene {cantidad} líneas.")
except FileNotFoundError:
    # Paso 6: Mensaje de error si el archivo no existe
    print("❌ Error: El archivo no fue encontrado. Verifica el nombre o la ubicación.")
