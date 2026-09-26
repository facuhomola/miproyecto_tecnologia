import sqlite3

conexion = sqlite3.connect("../basededatos/calificaciones.db")

cursor = conexion.cursor()

cursor.execute("""
    DELETE FROM estudiantes
    WHERE nro = ?
""", (999,))

conexion.commit()

print("Estudiante eliminado correctamente.")

conexion.close()