import ctypes
import hashlib
import mysql.connector
import sys
import dropbox
import requests
from cryptography.fernet import Fernet

# Credenciales de la aplicación
APP_KEY = 'p7604goq0hcg570'
APP_SECRET = '15qcohqd1pff6j8'
REFRESH_TOKEN = ''

# Variable global para almacenar datos del usuario
usr = None
id_user = None

# Variable para las credenciales de dropbox
ACCESS_TOKEN = 'sl.B8OhHWWgDi6jyRi3orJwpPkmopNJkMxnn-4o7QZ0hCBqwMFi-zshrc1Jnf-mbjt4dGfIU7duuvhDvaf0Ea9N_ozG3Nu0-zwKhNhxCD6rmbGykhCI9PUAdfvjohj04ALi-XJOwwvCBTT73Qw'
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def renovar_access_token():
    url = "https://api.dropboxapi.com/oauth2/token"
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN,
        'client_id': APP_KEY,
        'client_secret': APP_SECRET
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        new_access_token = response.json()['access_token']
        return new_access_token
    else:
        print("Error al renovar el Access Token:", response.json())
        return None

# Función para obtener la imagen de usuario de dropbox
def obtener_img_usr(dropbox_path):
    global dbx
    try:
        link = dbx.files_get_temporary_link(dropbox_path)
        return link.link
    except dropbox.exceptions.AuthError:
        new_access_token = renovar_access_token()
        print(new_access_token)
        if new_access_token:
            dbx = dropbox.Dropbox(new_access_token)
            link = dbx.files_get_temporary_link(dropbox_path)
            return link.link
        else:
            print("No se pudo renovar el Access Token")
            return None

# Función para desencriptar las credenciales
def desencriptar_credenciales():
    key = "xGqEkVe8ol9RIrZ7vTBITGHs4njqkRK2CXB19iGLlFM="
    encrypted_credentials = "gAAAAABmvgF9kxOfksqnszPY-vP3h23kZrKivC6NpVr-S6Y2IMK8SkSLpdJLqkLDrEz-z8xua60JhCgFyR5okTqrlHwXUPbHETEcKIXAYnRRPWw59ZWPZDEfR2X5WoJTGdy-QYebA6uUL8jI8RDDfG7UYppOyMBH38zduesezcx1gSYXOAx-LPriGUFKKEcnFPdLnf4xmmgQ"
    cipher_suite = Fernet(key)
    decrypted_credentials = cipher_suite.decrypt(encrypted_credentials).decode()
    credentials = {}
    for line in decrypted_credentials.split('\n'):
        if line:
            var, value = line.split('=')
            credentials[var] = value
    return credentials

# Función para conectar a la base de datos
def conexion():
    try:
        credentials = desencriptar_credenciales()
        conexion = mysql.connector.connect(
            host=credentials['host'],
            user=credentials['user'],
            password=credentials['password'],
            database=credentials['database'],
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
    page.window.close()

# Función para validar el usuario
def validar_usuario(user, password_hash):
    global id_user
    global usr
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

# Funciones para obtener datos de usuario
def obtener_id_actual():
    global id_user
    return id_user
def obtener_tipo_actual():
    global usr
    return usr

# Función para validar si el usuario está logueado
def is_logged(page):
    if id_user is None:
        page.clean()
        page.update()
        page.go("/")
        return False
    
# Función para saber si el usuario es administrador
def is_admin(page):
     if usr == "Administrativo":
        return True
     else:
        page.clean()
        page.update()
        page.go("/dashboard")
        return False

# Función para bloquear el login/register si el usuario ya está logueado      
def login_block(page):
    if id_user is not None:
        if usr == "Administrativo":
            page.clean()
            page.update()
            page.go("/admin")
        else:
            page.clean()
            page.update()
            page.go("/dashboard")
        return False

# Función para cerrar la sesión    
def cerrar_sesion(page):
    global id_user
    global usr
    id_user = None
    usr = None
    page.go("/")
    page.clean()
    page.update()
    return id_user, usr

# Función para ir atrás en la página 404
def go_back(page):
    if id_user == None:
        page.go("/")
    else:
        if usr == "Administrativo":
            page.clean()
            page.update()
            page.go("/admin")
        else:
            page.clean()
            page.update()
            page.go("/dashboard")