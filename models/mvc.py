# Importamos las librerias necesarias
import ctypes
import hashlib
import mysql.connector
import os

# Importamos las funciones necesarias
from dotenv import load_dotenv

from pages.index import user, password_hash

# Cargar las variables de entorno
load_dotenv()

# Funcion para conectar a la base de datos
def conexion ():
    try:
        conexion = mysql.connector.connect(
            host = os.getenv('host'),
            user = os.getenv('user'),
            password = os.getenv('password'),
            database = os.getenv('database'),
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la BD: {e}")
        return None
conn = conexion()



def cerrar_conexion(cursor, conn):
    cursor.close()
    conn.close()

# Obtener la resolución de la pantalla
user32 = ctypes.windll.user32
pantalla_ancho = user32.GetSystemMetrics(0)
pantalla_alto = user32.GetSystemMetrics(1)

def screenx(window_width):
    return (pantalla_ancho - window_width) // 2

def screeny(window_height):
    return (pantalla_alto - window_height) // 2

# Funcion para encriptar
def encriptar(contraseña):
    md5 = hashlib.md5(contraseña.encode()).hexdigest()
    sha256 = hashlib.sha256(md5.encode()).hexdigest()
    hash = hashlib.sha256(sha256.encode()).hexdigest()
    return hash

# Funcion para cerrar la ventana
def cerrar_app(page):
    page.window_close()

# Funcion para iniciar sesion a partir de los valores de usuario y contraseña de otro archivo
def login(username, password_hash, page, tipo_user):
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return
        
        # Creamos el cursor
    cursor = conn.cursor()

        # Verificamos si el usuario existe
    cursor.execute(f"SELECT * FROM users WHERE usuario = '{username}' AND contraseña = '{password_hash}'")
    respuesta = cursor.fetchone()

        # Si el usuario existe
    if respuesta:
            # Verificamos el tipo de usuario
        if tipo_user == "Admin":
            cursor.execute(f"SELECT * FROM users WHERE usuario = '{user}' AND tipo = '{tipo_user}'")
            tipo_usr = cursor.fetchone()
            if tipo_usr:
                page.update()
                page.go("/admin")
                page.update()
            else:
                #open_error_permisos(e)
                pass
        else:
            page.update()
            page.go("/dashboard")
            page.update()
    else:
        #open_error_user(e)
        pass

