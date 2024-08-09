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

# Función para ver proyectos del usuario
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
    
# Función para obtener el correo del usuario actual
def correo_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT correo_electronico FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta

# Función para obtener la contraseña del usuario actual
def contraseña_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT contrasena FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Función para obtener la imagen del usuario actual
def imagen_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT imagen FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Función para obtener el tipo de usuario
def tipo_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT tipo_usuario FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta