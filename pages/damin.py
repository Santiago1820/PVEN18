# importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.mvc import *
from models.pages import *
from models.query import *
from config.settings import titulo, tema, logo

# Codigo de la funcion RegisterPage
def Dadmin(page: ft.Page):
    nombre = nombre_usuario()[0]
    # Definir las propiedades de la pagina
    page.window_title_bar_hidden = False
    page.window_maximized = True
    page.title = titulo
    page.theme_mode = tema
    page.padding = 0
    # Codigo de la pagina de registro
    page.add(
        ft.Text(f"Bienvenido al panel administrativo {nombre[0]}", size=20),
        )