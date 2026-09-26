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
            print("\nAlta de estudiante")

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
            print("\nAlta de materia")

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