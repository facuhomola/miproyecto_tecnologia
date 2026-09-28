from basededatos.conexion import conectar


def insertar_materia(nombre_materia, curso, docente):

    conexion = conectar()

    try:

        cursor = conexion.cursor()

        consulta = """
            INSERT INTO materias (nombre_materia, curso, docente)
            VALUES (?, ?, ?)
        """

        cursor.execute(consulta, (nombre_materia, curso, docente))

        conexion.commit()

        return True, ""

    except Exception as error:

        conexion.rollback()

        mensaje = str(error)

    finally:

        conexion.close()

# Función para listar todas las materias
def listar_materias():
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        consulta = """
            SELECT id_materia, nombre_materia, curso, docente
            FROM materias
            ORDER BY curso ASC, nombre_materia ASC
        """

        cursor.execute(consulta)

        materias = cursor.fetchall()

        return materias

    finally:
        conexion.close()