# importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.pages import *
from config.settings import *
from models.mvc import *
from models.query import *
from sources.menu import *

# Codigo de la funcion Clientes
def Clients(page: ft.Page):
    page.clean()
    page.update()
    if is_logged(page) is not False: 
        nombre = nombre_usuario()[0]
        proyectos = proyectos_usuario()
        # Definir las propiedades de la pagina
        page.window_title_bar_hidden = False
        page.window_maximized = True
        page.title = titulo
        page.theme_mode = tema
        page.padding = 0
        page.add(ft.Row([
            ft.Column([
                ft.Text(f"{nombre_app}", size=30),
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
                    ft.Text(f"Clientes", size=40),
                    ft.Text(f"Proyectos {proyectos}", size=20),
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