#Ejercicio 4 Lector de datos CSV
# Paso 1: Abrir el archivo CSV en modo lectura
try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        print("📦 Lista de productos:\n")

        # Paso 2: Recorrer el archivo línea por línea
        for linea in archivo:
            # Paso 3: Eliminar salto de línea final
            linea = linea.strip()

            # Paso 4: Separar los valores por coma
            datos = linea.split(",")

            # Verificar que hay exactamente 3 datos
            if len(datos) == 3:
                nombre, precio, stock = datos

                # Paso 5: Imprimir datos ordenadamente
                print(f"Producto: {nombre} | Precio: ${precio} | Stock: {stock} unidades")
            else:
                print("❌ Línea con formato incorrecto:", linea)

except FileNotFoundError:
    print("❌ Error: El archivo 'productos.csv' no fue encontrado.")
