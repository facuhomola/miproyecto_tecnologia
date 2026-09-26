from basededatos.conexion import conectar


def insertar_estudiante(nro, nombre_apellido, dni):

    conexion = conectar()

    try:

        cursor = conexion.cursor()

        consulta = """
            INSERT INTO estudiantes (nro, nombre_apellido, dni)
            VALUES (?, ?, ?)
        """

        cursor.execute(consulta, (nro, nombre_apellido, dni))

        conexion.commit()

        return True, ""

    except Exception as error:

        conexion.rollback()

        mensaje = str(error)

        if "estudiantes.nro" in mensaje:

            return False, f"El número de registro {nro} ya está registrado."

        elif "estudiantes.dni" in mensaje:

            return False, f"El DNI {dni} ya está registrado."

        else:

            return False, "No se pudo registrar el estudiante."

    finally:

        conexion.close()