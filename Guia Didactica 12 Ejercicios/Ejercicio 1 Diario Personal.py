#Ejercicio 1 Diario Personal
import datetime

# Paso 2: Solicitar entrada del usuario
entrada = input("✍️ Escribe tu entrada del diario:\n")

# Paso 1: Obtener fecha y hora actual
ahora = datetime.datetime.now()
fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")

# Paso 3 y 4: Abrir archivo y escribir entrada con fecha y hora
with open("diario.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"[{fecha_hora}]\n{entrada}\n\n")

# Paso 5: (se hace automáticamente con 'with')
# Paso 6: Confirmación
print("✅ Entrada guardada en diario.txt.")
