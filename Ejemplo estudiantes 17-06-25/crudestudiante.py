import os
#Se importa el módulo para usar la función: os.path.exist(ruta)
ARCHIVO="estudiantes.txt"


def cargar_estudiantes():
    estudiantes=[]
#La funcion os.path.exist() verifica si un archivo o carpeta existe en una ruta determinada
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera=linea.strip().split(',')
            #Linea.strip() elimina espacios y saltos de linea (\n) al principio o al final.
            #Split(",") divide la cadena en una lista de partes, usando la coma como separador.
            estudiantes.append({
                "codigo": codigo,
                "nombre": nombre,
                "apellido": apellido,
                "carrera": carrera
            })
    return estudiantes


def guardar_estudiantes(estudiantes):
    with open(ARCHIVO, "w") as archivo:
        for est in estudiantes:
            linea=f"{est['codigo']},{est['nombre']},{est['apellido']},{est['carrera']}\n"
            archivo.write(linea)


def crear_estudiante(estudiantes):
    codigo=input("Codigo del estudiante: ")
    #Verificar si el codigo ya existe
    #La funcion any() devuelve true si al menos un elemento de un iterable es verdadero.
    if any(est["codigo"]==codigo for est in estudiantes):
        print("El codigo ya existe\n")
        return
    
    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    carrera=input("Carrera: ")

    estudiantes.append({
        "codigo":codigo,
        "nombre":nombre,
        "apellido":apellido,
        "carrera":carrera
    })
    guardar_estudiantes(estudiantes)
    print("Estudiante agregado correctamente.\n")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    
    print("\nLista de estudiantes:")
    for est in estudiantes:
        print(f"Codigo: {est['codigo']}, Nombre: {est['nombre']}, Apellido: {est['apellido']}, Carrera: {est['carrera']}")
    print()
    
def actualizar_estudiante(estudiantes):
    codigo=input("Ingresa el codigo del estudiante a actualizar: ")
    for est in estudiantes:
       if est["codigo"]==codigo:
           est["nombre"]==input(f"Nuevo nombre (actual: {est['nombre']}):") or est['nombre']
           est["apellido"]==input(f"Nuevo apellido (actual: {est['apellido']}):") or est['apellido']
           est["carrera"]==input(f"Nueva carrera (actual: {est['carrera']}):") or est['carrera']
           guardar_estudiantes(estudiantes)
           print("Estudiantes actualizadi.\n")
           return
print("No se encontro estudiante con ese codigo.\n")

def eliminar_estudiante(estudiantes):
    codigo=input("Ingresa el codigo del estudiante a eliminar: ")
    for est in estudiantes:
        if est["codigo"]==codigo:
            estudiantes.remove(est)
            guardar_estudiantes(estudiantes)
            print("Estudiante eliminado.\n")
            return
    print("No se encontro estudiante con ese codigo.\n")
    
#Funcion menu principal
def menu():
    estudiantes=cargar_estudiantes()
    while True:
        print("====== MENU CRUD ESTUDIANTES =====")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion=input("Selecciona una opcion (1-5): ")
        
        if opcion=="1":
            crear_estudiante(estudiantes)
        elif opcion=="2":
            mostrar_estudiantes(estudiantes)
        elif opcion=="3":
            actualizar_estudiante(estudiantes)
        elif opcion=="4":
            eliminar_estudiante(estudiantes)
        elif opcion=="5":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. \n")
  
            
#Instruccion para ejecutar el menu
menu()