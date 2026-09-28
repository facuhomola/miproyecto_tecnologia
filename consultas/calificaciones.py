from basededatos.conexion import conectar

# Función para insertar una calificación en la base de datos
def insertar_calificacion(id_estudiante, id_materia, nota_primer_trimestre, nota_segundo_trimestre, nota_tercer_trimestre, nota_examen_diciembre, nota_examen_marzo, observaciones):

    conexion = conectar()

    try:

        cursor = conexion.cursor()

        consulta = """
            INSERT INTO calificaciones (id_estudiante, id_materia, nota_primer_trimestre, nota_segundo_trimestre, nota_tercer_trimestre, nota_examen_diciembre, nota_examen_marzo, observaciones)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(consulta, (id_estudiante, id_materia, nota_primer_trimestre, nota_segundo_trimestre, nota_tercer_trimestre, nota_examen_diciembre, nota_examen_marzo, observaciones))

        conexion.commit()

        return True, ""
    
    except Exception as error:

        conexion.rollback()

        mensaje = str(error)

        if "UNIQUE constraint failed" in mensaje:
            return False, "Ya existe una calificación para este estudiante y esta materia."

        elif "FOREIGN KEY constraint failed" in mensaje:
            return False, "El estudiante o la materia no existen."

        else:
            return False, "No se pudo registrar la calificación."

    finally:

        conexion.close()

# Función para buscar una calificación por estudiante y materia
def buscar_calificacion(id_estudiante, id_materia):

    conexion = conectar()

    try:

        cursor = conexion.cursor()

        consulta = """
            SELECT *
            FROM calificaciones
            WHERE id_estudiante = ? AND id_materia = ?
        """

        cursor.execute(consulta, (id_estudiante, id_materia))

        calificacion = cursor.fetchone()

        return calificacion

    finally:

        conexion.close()

# Función para eliminar una calificación por su ID
def eliminar_calificacion(id_calificacion):

    conexion = conectar()

    try:
        cursor = conexion.cursor()

        consulta = """
            DELETE FROM calificaciones
            WHERE id_calificacion = ?
        """

        cursor.execute(consulta, (id_calificacion,))
        conexion.commit()

        return True, ""
    
    except Exception as error:
        conexion.rollback()
        return False, str(error)

    finally:
        conexion.close()