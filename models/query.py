# Importamos las funciones necesarias
from models.mvc import *

# Variables globales
id_proy = None
id_tarea = None

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
     
# Función para obtener nombre de un cliente
def nombre_clientes_usuario():
    id_us = obtener_id_actual()
    conn = conexion()
    if conn is None:        
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
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT direccion FROM Clientes WHERE _id = '{id_us}'")
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