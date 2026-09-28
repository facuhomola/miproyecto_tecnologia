from basededatos.conexion import conectar

# Función para insertar un estudiante en la base de datos
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

        #else:

         #   return False, "No se pudo registrar el estudiante."
        else:

            return False, f"No se pudo registrar el estudiante: {mensaje}"

    finally:

        conexion.close()
    
# Función para buscar por número de registro
def buscar_estudiante_por_nro(nro):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        consulta = """
            SELECT id_estudiante, nro, nombre_apellido, dni
            FROM estudiantes
            WHERE nro = ?
        """

        cursor.execute(consulta, (nro,))

        estudiante = cursor.fetchone()

        return estudiante

    finally:
        conexion.close()

# Función para buscar por dni
def buscar_estudiante_por_dni(dni):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        consulta = """
            SELECT id_estudiante, nro, nombre_apellido, dni
            FROM estudiantes
            WHERE dni = ?
        """

        cursor.execute(consulta, (dni,))

        estudiante = cursor.fetchone()

        return estudiante

    finally:
        conexion.close()


def eliminar_estudiante(id_estudiante):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        consulta = """
            DELETE FROM estudiantes
            WHERE id_estudiante = ?
        """

        cursor.execute(consulta, (id_estudiante,))

        conexion.commit()

        return True, ""

    except Exception as error:

        conexion.rollback()

        mensaje = str(error)

        if "FOREIGN KEY" in mensaje:

            return False, "No se puede eliminar el estudiante porque tiene calificaciones registradas."

        else:

            return False, "No se pudo eliminar el estudiante."

    finally:
        conexion.close()