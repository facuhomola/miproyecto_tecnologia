import sqlite3

conexion = sqlite3.connect("../basededatos/calificaciones.db")

cursor = conexion.cursor()

cursor.execute("""
    SELECT id_estudiante, nro, nombre_apellido, dni
    FROM estudiantes
    WHERE nro = ?
""", (999,))

estudiante = cursor.fetchone()

print(estudiante)

conexion.close()