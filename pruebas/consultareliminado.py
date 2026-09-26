import sqlite3

conexion = sqlite3.connect("../basededatos/calificaciones.db")

cursor = conexion.cursor()

cursor.execute("""
    SELECT *
    FROM estudiantes
    WHERE nro = ?
""", (999,))

resultado = cursor.fetchone()

print("Resultado:", resultado)