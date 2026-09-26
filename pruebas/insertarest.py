import sqlite3

conexion = sqlite3.connect("../basededatos/calificaciones.db")

cursor = conexion.cursor()

cursor.execute("""
    INSERT INTO estudiantes (nro, nombre_apellido, dni)
    VALUES (?, ?, ?)
""", (999, "Estudiante Prueba", 99999999))

conexion.commit()

print("Estudiante agregado correctamente.")

conexion.close()