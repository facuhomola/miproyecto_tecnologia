import sqlite3

conexion = sqlite3.connect("../basededatos/calificaciones.db")

cursor = conexion.cursor()

cursor.execute("""
    SELECT id_estudiante, nro, nombre_apellido, dni
    FROM estudiantes
    ORDER BY nro
""")

estudiantes = cursor.fetchall()

print("=== LISTADO DE ESTUDIANTES ===")

for estudiante in estudiantes:
    print(
        f"ID: {estudiante[0]} | "
        f"Nro: {estudiante[1]} | "
        f"Nombre: {estudiante[2]} | "
        f"DNI: {estudiante[3]}"
    )

conexion.close()