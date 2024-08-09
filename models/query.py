from models.mvc import *

# Función para obtener el nombre del usuario actual
def nombre_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT nombre FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta

# Función para ver un proyecto del usuario
def proyectos_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Proyectos WHERE usuario_id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta