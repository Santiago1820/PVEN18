# Importamos las librerías necesarias
import ctypes
import hashlib
import mysql.connector
import os

# Importamos las funciones necesarias
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Variable global para almacenar datos del usuario
id_user = None

# Función para conectar a la base de datos
def conexion():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv('host'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            database=os.getenv('database'),
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la BD: {e}")
        return None

# Función para cerrar la conexión
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

# Función para encriptar
def encriptar(contraseña):
    md5 = hashlib.md5(contraseña.encode()).hexdigest()
    sha256 = hashlib.sha256(md5.encode()).hexdigest()
    hash = hashlib.sha256(sha256.encode()).hexdigest()
    return hash

# Función para cerrar la ventana
def cerrar_app(page):
    page.window_close()

# Función para validar el usuario
def validar_usuario(user, password_hash):
    global id_user
    conn = conexion()
    if conn is None:
        print("Error al conectar a la base de datos")
        return None
    else:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Usuarios WHERE correo_electronico = '{user}' AND contrasena = '{password_hash}'")
        respuesta = cursor.fetchone()
        if respuesta:
            usr = respuesta[4]
            id_user = respuesta[0]
            cerrar_conexion(cursor, conn)
            return usr, id_user
        else:
            cerrar_conexion(cursor, conn)
            return None

# Función para obtener datos de usuario
def obtener_id_actual():
    global id_user
    return id_user
