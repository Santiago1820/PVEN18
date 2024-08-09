# importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.pages import *
from config.settings import *
from models.mvc import *
from models.query import *


# Codigo de la funcion RegisterPage
def Dashboard(page: ft.Page):
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
            ft.Text("Dashboard", size=30),
            ft.Row([
                ft.ElevatedButton("Salir", icon="logout", icon_color="red", color="red", bgcolor="TRANSPARENT" ,on_click=lambda _: cerrar_app(page)),
            ]),
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.START,
        ), # Menú lateral
        ft.Row([
            ft.Container(
                ft.Column([
                ft.Text(f"Bienvenido a {nombre_app} {nombre[0]}", size=40),
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