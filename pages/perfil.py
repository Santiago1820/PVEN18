# Importar las librerias necesarias
import flet as ft

# Importar las funciones necesarias
from models.pages import *
from config.settings import *
from models.mvc import *
from models.query import *
from sources.menu import *

# Codigo de la funcion Profile
def Profile(page: ft.Page):
    page.clean()
    page.update()
    if is_logged(page) is not False:
        nombre = nombre_usuario()[0]
        correo = correo_usuario()[0]
        contraseña = contraseña_usuario()[0]
        imagen = imagen_usuario()[0]
        # Definir las propiedades de la pagina
        page.window_title_bar_hidden = False
        page.window_maximized = True
        page.title = titulo
        page.theme_mode = tema
        page.padding = 0
        page.add(ft.Row([
            ft.Column([
                ft.Text("Me", size=30),
                ft.Row([
                    ft.Column([
                    menu(page),
                    ]),
                ]),
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.START,
            ), # Menú lateral
            ft.Row([
                ft.Container(
                    ft.Column([
                    ft.Text(f"Mi perfil", size=40),
                    ft.Container(
                        ft.Image(
                            src= f"../{imagen[0]}",
                            width=200,
                            height=200,),
                    ),
                    ft.Text(f"Nombre: {nombre[0]}", size=20),
                    ft.Text(f"Correo Electrónico: {correo[0]}", size=20),
                    ]),
                ),
            ],
            spacing=30,
            alignment="spaceBetween",
            ), # Contenido
        ],
        spacing=30,
        alignment="start",
        ))
    page.update()