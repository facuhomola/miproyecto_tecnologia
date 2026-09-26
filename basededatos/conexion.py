import sqlite3

def conectar():
    conexion = sqlite3.connect("basededatos/calificaciones.db")
    return conexion