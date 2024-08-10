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
        cursor.execute(f"SELECT nombre FROM Proyectos WHERE usuario_id = '{id_us}'")
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
    
# Función para obtener el titulo de una tarea
def tareas_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT titulo FROM Tareas WHERE usuario_id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Función para obtener descripcion de una tarea 
def descripcion_tareas_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT descripcion FROM Tareas WHERE usuario_id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Función para obtener la fecha_creacion de una tarea
def fecha_creacion_tareas_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT fecha_creacion FROM Tareas WHERE usuario_id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Función para obtener la fecha_vencimiento de una tarea
def fecha_vencimiento_tareas_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT fecha_vencimiento FROM Tareas WHERE usuario_id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta   
         
# Función para obtener el estado de una tarea
def estado_tareas_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT estado FROM Tareas WHERE usuario_id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta    
    
# Función para obtener la prioridad de una tarea
def prioridad_tareas_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT fecha_vencimiento FROM Tareas WHERE usuario_id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
     
# Función para obtener nombre de un cliente
def nombre_clientes_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT nombre FROM Clientes WHERE _id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta   
                           
# Función para obtener el correo_electronico de un cliente
def clientes_clientes_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT correo_electronico FROM Clientes WHERE _id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta   
# Función para obtener el telofono de los clientes
def telefono_clientes_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT telefono FROM Clientes WHERE _id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta  
          
# Función para obtener la direccion de los clientes   
def direccion_clientes_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT direccion FROM Clientes WHERE _id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta 
    
# Función para obtener el id de el proyecto
def id_proyecto_usuario(p):
    global id_proy
    proy = p
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT id_proyecto FROM Proyectos WHERE nombre= '{proy}'")
        respuesta = cursor.fetchall()
        if respuesta:
            id_proy = respuesta[0]
            cerrar_conexion(cursor, conn)
            return id_proy
        else:
            cerrar_conexion(cursor, conn)
            return None 

# Función para guardar id de el proyecto
def guardar_id_proyecto():
    global id_proy
    return id_proy 
