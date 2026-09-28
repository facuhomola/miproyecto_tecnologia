# Funciones para altas y bajas de estudiantes, materias y calificaciones
from consultas.estudiantes import insertar_estudiante
from consultas.materias import insertar_materia
from consultas.estudiantes import buscar_estudiante_por_nro
from consultas.estudiantes import buscar_estudiante_por_dni
from consultas.estudiantes import eliminar_estudiante
from consultas.materias import listar_materias
from consultas.calificaciones import insertar_calificacion
from consultas.calificaciones import existe_calificacion
from consultas.materias import eliminar_materia

# ----------------------------------------------------------------

# OPERACIONES PARA ALTA DE ESTUDIANTES, MATERIAS Y CALIFICACIONES

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

# ----------------------------------------------------------------

# Función para buscar estudiante por número de registro o por DNI
def buscar_estudiante():

    print("\n--- BUSCAR ESTUDIANTE ---")
    print("1. Buscar por NRO")
    print("2. Buscar por DNI")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":

        nro = input("Ingrese NRO de registro: ").strip()

        if not nro.isdigit():
            print("El NRO debe contener solamente números.")
            return None

        estudiante = buscar_estudiante_por_nro(int(nro))

    elif opcion == "2":

        dni = input("Ingrese DNI: ").strip()

        if not dni.isdigit():
            print("El DNI debe contener solamente números.")
            return None

        estudiante = buscar_estudiante_por_dni(int(dni))

    else:
        print("Opción inválida.")
        return None

    if estudiante:

        print("\n--- ESTUDIANTE ENCONTRADO ---")
        print(f"NRO: {estudiante[1]}")
        print(f"Nombre y apellido: {estudiante[2]}")
        print(f"DNI: {estudiante[3]}")

        return estudiante

    else:

        print("\nNo se encontró ningún estudiante.")
        return None
# Fin de la función buscar_estudiante

# ----------------------------------------------------------------

# Función para validar que la nota esté entre 0 y 10
def validar_nota(nota):

    try:
        nota = float(nota)

        if nota < 0 or nota > 10:
            return False

        return True

    except ValueError:
        return False
# Fin de la función validar_nota

# ----------------------------------------------------------------

# Función para dar de alta una calificación
def alta_calificacion():

    estudiante = buscar_estudiante()

    if estudiante is None:
        return

    id_estudiante = estudiante[0] # Para obtener el id_estudiante del estudiante encontrado

    materias = listar_materias()

    if not materias:
        print("\nNo hay materias cargadas.")
        return

    print("\n--- MATERIAS ---")

    for i, materia in enumerate(materias, start=1):
        print(f"{i}. {materia[1]} - Curso: {materia[2]} - Docente: {materia[3]}")

    opcion = input("\nSeleccione una materia: ").strip()

    if not opcion.isdigit():
        print("Debe ingresar un número.")
        return

    opcion = int(opcion)

    if opcion < 1 or opcion > len(materias):
        print("La opción seleccionada no existe.")
        return

    materia_seleccionada = materias[opcion - 1]

    id_materia = materia_seleccionada[0] # Para obtener el id_materia de la materia seleccionada

    print(f"\nMateria seleccionada: {materia_seleccionada[1]}")

    if existe_calificacion(id_estudiante, id_materia): # Llama a a la función existe_calificacion para verificar si ya existe una calificación para el estudiante y materia seleccionados

        print("\nYa existe una calificación para este estudiante y esta materia.")
        print("Utilice la opción de actualización para modificarla.")

        return

    # Carga de calificaciones

    print("\n--- CARGA DE CALIFICACIONES ---")
    print("Si una nota todavía no fue cargada, ingrese 0.")
    print("Más adelante podrá actualizar las calificaciones.")
    print()

    nota_primer_trimestre = input("Nota de primer trimestre: ").strip()
    if not validar_nota(nota_primer_trimestre):
        print("\nLa nota del primer trimestre debe estar entre 0 y 10.")
        return

    nota_segundo_trimestre = input("Nota de segundo trimestre: ").strip()
    if not validar_nota(nota_segundo_trimestre):
        print("\nLa nota del segundo trimestre debe estar entre 0 y 10.")
        return

    nota_tercer_trimestre = input("Nota de tercer trimestre: ").strip()
    if not validar_nota(nota_tercer_trimestre):
        print("\nLa nota del tercer trimestre debe estar entre 0 y 10.")
        return

    nota_examen_diciembre = input("Nota examen de diciembre: ").strip()
    if not validar_nota(nota_examen_diciembre):
        print("\nLa nota del examen de diciembre debe estar entre 0 y 10.")
        return

    nota_examen_marzo = input("Nota examen de marzo: ").strip()
    if not validar_nota(nota_examen_marzo):
        print("\nLa nota del examen de marzo debe estar entre 0 y 10.")
        return

    observaciones = input("Observaciones (opcional): ").strip() 
    
    registro_exitoso, mensaje = insertar_calificacion(id_estudiante, id_materia, nota_primer_trimestre, nota_segundo_trimestre, nota_tercer_trimestre, nota_examen_diciembre, nota_examen_marzo, observaciones)

    if registro_exitoso:
        print("\nCalificación registrada correctamente.")
    else:
        print(f"\nError: {mensaje}")

# Fin de la función alta_calificacion

# ----------------------------------------------------------------

# OPERACIONES PARA BAJA DE ESTUDIANTES, MATERIAS Y CALIFICACIONES

# BAJA PARA ESTUDIANTES
def baja_estudiante():

    print("\n--- BAJA DE ESTUDIANTE ---")

    estudiante = buscar_estudiante()

    if estudiante is None:
        return

    print("\n¿Desea eliminar este estudiante?")
    confirmacion = input("Ingrese S para confirmar o N para cancelar: ").strip().upper()

    if confirmacion != "S":
        print("Operación cancelada.")
        return

    resultado, mensaje = eliminar_estudiante(estudiante[0])

    if resultado:
        print("Estudiante eliminado correctamente.")
    else:
        print(mensaje)
# FIN BAJA PARA ESTUDIANTES

# ----------------------------------------------------------------

# BAJA PARA MATERIAS
def baja_materia():

    print("\n--- BAJA DE MATERIA ---")

    materias = listar_materias()

    if not materias:
        print("\nNo hay materias cargadas.")
        return

    print("\n--- MATERIAS ---")

    for i, materia in enumerate(materias, start=1):
        print(f"{i}. {materia[1]} - Curso: {materia[2]} - Docente: {materia[3]}")

    opcion = input("\nSeleccione una materia para eliminar: ").strip()

    if not opcion.isdigit():
        print("Debe ingresar un número.")
        return

    opcion = int(opcion)

    if opcion < 1 or opcion > len(materias):
        print("La opción seleccionada no existe.")
        return

    materia_seleccionada = materias[opcion - 1]

    print(f"\nMateria seleccionada: {materia_seleccionada[1]}")

    confirmacion = input("Ingrese S para confirmar la eliminación o N para cancelar: ").strip().upper()

    if confirmacion != "S":
        print("Operación cancelada.")
        return

    resultado, mensaje = eliminar_materia(materia_seleccionada[0])

    if resultado:
        print("Materia eliminada correctamente.")
    else:
        print(mensaje)
# FIN BAJA PARA MATERIAS

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
            baja_estudiante()
            #print("\nBaja de estudiante")

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
            baja_materia()
            #print("\nBaja de materia")

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
            alta_calificacion()
            #print("\nAlta de calificación")

        elif opcion == "2":
            print("\nBaja de calificación")

        elif opcion == "0":
            break

        else:
            print("\nOpción incorrecta.")