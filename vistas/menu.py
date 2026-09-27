# Funciones para altas y bajas de estudiantes, materias y calificaciones
from consultas.estudiantes import insertar_estudiante
from consultas.materias import insertar_materia

# ----------------------------------------------------------------

# ALTA PARA ESTUDIANTES
def alta_estudiante():

    print("\n=== ALTA DE ESTUDIANTE ===")

    # Número de registro
    while True:

        nro = input("Número de registro: ")

        if nro.isdigit() and int(nro) > 0:
            nro = int(nro)
            break

        print("Error: el número de registro debe ser un número mayor que 0.")

    # Nombre y apellido
    while True:

        nombre_apellido = input("Nombre y apellido: ").strip()

        if nombre_apellido:
            break

        print("Error: debe ingresar el nombre y apellido.")

    # DNI
    while True:

        dni = input("DNI: ")

        if dni.isdigit() and int(dni) > 0:
            dni = int(dni)
            break

        print("Error: el DNI debe ser un número mayor que 0.")

    print("\nDatos ingresados correctamente:")
    print("Número de registro:", nro)
    print("Nombre y apellido:", nombre_apellido)
    print("DNI:", dni)

   # insertar_estudiante(nro, nombre_apellido, dni)
   # print("\nEstudiante registrado correctamente.")

    resultado, mensaje = insertar_estudiante(nro, nombre_apellido, dni)

    if resultado:

        print("\nEstudiante registrado correctamente.")

    else:

        print("\nNo se pudo registrar el estudiante.")
        print("Error:", mensaje)

# FIN ALTA PARA ESTUDIANTES

# ----------------------------------------------------------------

# ALTA PARA MATERIAS
def alta_materia():

    print("\n=== ALTA DE MATERIA ===")

    # Nombre de la materia
    while True:

        nombre_materia = input("Nombre de la materia: ").strip()

        if nombre_materia:
            break

        print("Error: debe ingresar el nombre de la materia.")

    # Curso
    while True:

        curso = input("Curso: ").strip()

        if curso:
            break

        print("Error: debe ingresar el curso.")

    # Docente
    while True:

        docente = input("Docente: ").strip()

        if docente:
            break

        print("Error: debe ingresar el nombre del docente.")

    print("\nDatos ingresados correctamente:")
    print("Nombre de la materia:", nombre_materia)
    print("Curso:", curso)
    print("Docente:", docente)

    resultado, mensaje = insertar_materia(nombre_materia, curso, docente)

    if resultado:

        print("\nMateria registrada correctamente.")

    else:

        print("\nNo se pudo registrar la materia.")
        print("Error:", mensaje)
# FIN ALTA PARA MATERIAS

# MENU PRINCIPAL
def menu_principal():

    while True:

        print("\n================================")
        print("     SISTEMA DE CALIFICACIONES")
        print("================================")
        print("1. Estudiantes")
        print("2. Materias")
        print("3. Calificaciones")
        print("0. Salir")
        print("================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_estudiantes()

        elif opcion == "2":
            menu_materias()

        elif opcion == "3":
            menu_calificaciones()

        elif opcion == "0":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción incorrecta.")


def menu_estudiantes():

    while True:

        print("\n================================")
        print("          ESTUDIANTES")
        print("================================")
        print("1. Alta de estudiante")
        print("2. Baja de estudiante")
        print("0. Volver")
        print("================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_estudiante()

        elif opcion == "2":
            print("\nBaja de estudiante")

        elif opcion == "0":
            break

        else:
            print("\nOpción incorrecta.")


def menu_materias():

    while True:

        print("\n================================")
        print("            MATERIAS")
        print("================================")
        print("1. Alta de materia")
        print("2. Baja de materia")
        print("0. Volver")
        print("================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_materia()

        elif opcion == "2":
            print("\nBaja de materia")

        elif opcion == "0":
            break

        else:
            print("\nOpción incorrecta.")


def menu_calificaciones():

    while True:

        print("\n================================")
        print("        CALIFICACIONES")
        print("================================")
        print("1. Alta de calificación")
        print("2. Baja de calificación")
        print("0. Volver")
        print("================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nAlta de calificación")

        elif opcion == "2":
            print("\nBaja de calificación")

        elif opcion == "0":
            break

        else:
            print("\nOpción incorrecta.")