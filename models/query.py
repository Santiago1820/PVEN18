# Importamos las funciones necesarias
from models.mvc import *

# Variables globales
id_proy = None
id_tarea = None

# Funcion de register y Recuperar contraseña
#-------------------------------------------#
# Función para registrar un usuario
def is_registered(correo):
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT correo_electronico FROM Usuarios WHERE correo_electronico = '{correo}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta

def registrar_usuario(nombre, user, contraseña):
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `Usuarios` (`nombre`, `correo_electronico`, `contrasena`) VALUES ('{nombre}','{user}','{contraseña}')")
        conn.commit()
        cerrar_conexion(cursor, conn)
        return True

# Funciones para los datos del Usuario
#-------------------------------------#
# Función para obtener el nombre del usuario actual
def nombre_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:       
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT nombre FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta

# Función para obtener el correo del usuario actual
def correo_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:       
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT correo_electronico FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta

# Función para obtener la imagen del usuario actual
def imagen_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT imagen FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Función para obtener la contraseña del usuario actual
def contraseña_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT contrasena FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Función para obtener el tipo de usuario
def tipo_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT tipo_usuario FROM Usuarios WHERE id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Funciones para los datos de los Proyectos y tareas
# ---------------------------------------- #    
# Función para ver proyectos del usuario
def proyectos_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT nombre FROM Proyectos WHERE usuario_id = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
    
# Función para obtener el titulo de una tarea
def tareas_usuario():
    id_p = guardar_id_proyecto()[0]
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT titulo FROM Tareas WHERE id_proyecto = '{id_p}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Función para obtener la tarea mediante el id
def info_tarea():
    id_t = guardar_id_tarea()[0]
    conn = conexion()
    if conn is None:       
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Tareas WHERE id = '{id_t}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta

# Funcion para obtener el nombre de un proyecto
def nombre_proyecto():
    id_p = guardar_id_proyecto()[0]
    conn = conexion()
    if conn is None:
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT nombre FROM Proyectos WHERE id_proyecto = '{id_p}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta    
     
# Función para obtener clientes del usuario
def clientes_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Clientes WHERE id_usuario = '{id_us}'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta   

# Funciones para los proyectos y tareas
# ------------------------------------ #  
# Función para obtener el id de el proyecto
def id_proyecto_usuario(p):
    global id_proy
    proy = p
    conn = conexion()
    if conn is None:        
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
        
# Función para obtener el id de la tarea
def id_tarea_usuario(t):
    global id_tarea
    tar = t
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM Tareas WHERE titulo = '{tar}'")
        respuesta = cursor.fetchall()
        if respuesta:
            id_tarea = respuesta[0]
            cerrar_conexion(cursor, conn)   
            return id_tarea
        else:
            cerrar_conexion(cursor, conn)
            return None 
        
# Funciones para los reportes
#----------------------------#
# Funcion para obtener las tareas pendientes
def tareas_pendientes():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT titulo, fecha_vencimiento FROM Tareas WHERE usuario_id = '{id_us}' AND estado = 'Pendiente'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Funcion para obtener las tareas en progreso
def tareas_progreso():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT titulo, fecha_vencimiento FROM Tareas WHERE usuario_id = '{id_us}' AND estado = 'En Progreso'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
# Funcion para obtener las tareas terminadas
def tareas_terminadas():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT titulo FROM Tareas WHERE usuario_id = '{id_us}' AND estado = 'Completa'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta

# Funciones para las notificaciones
#---------------------------------#
# Función para obtener las notificaciones sin leer
def notificaciones_sin_leer():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT a.*, b.titulo FROM Notificaciones a JOIN Tareas b ON b.id = a.tarea_id WHERE a.usuario_id = '{id_us}' AND a.leida ='0'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta
    
def notificaciones_leidas():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT a.*, b.titulo FROM Notificaciones a JOIN Tareas b ON b.id = a.tarea_id WHERE a.usuario_id = '{id_us}' AND a.leida ='1'")
        respuesta = cursor.fetchall()
        cerrar_conexion(cursor, conn)
        return respuesta

# Funciones para las variables globales
#--------------------------------------#
# Función para guardar id de el proyecto
def guardar_id_proyecto():
    global id_proy
    return id_proy 
# Función para guardar id de el proyecto
def guardar_id_tarea():
    global id_tarea
    return id_tarea