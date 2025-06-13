#Ejercicio 3 Generador de listas de compras
# Paso 1: Abrir el archivo en modo escritura ('w') para empezar una nueva lista
with open("compras.txt", "w", encoding="utf-8") as archivo:
    print("🛒 Generador de lista de compras")
    print("Escribe los productos uno por uno. Escribe 'fin' para terminar.\n")

    # Paso 2: Bucle infinito
    while True:
        # Paso 3: Pedir al usuario un producto
        producto = input("➤ Producto: ")

        # Paso 4: Verificar si se desea terminar
        if producto.strip().lower() == "fin":
            break

        # Paso 5: Escribir el producto en el archivo
        archivo.write(producto + "\n")

# Paso 6: Notificación final
print("✅ Lista de compras guardada en 'compras.txt'.")
