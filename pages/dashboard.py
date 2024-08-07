# importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.pages import *
from config.settings import titulo, tema, logo
from models.mvc import *

# Codigo de la funcion RegisterPage
def Dashboard(page: ft.Page):
    usuario = obtener_usuario_actual()
    # Definir las propiedades de la pagina
    page.window_title_bar_hidden = False
    page.window_maximized = True
    page.title = titulo
    page.theme_mode = tema
    page.padding = 0
    page.add(ft.Row([
        ft.Column([
            ft.Text("Dashboard", size=30),
            ft.Text(f"Bienvenido al dashboard {usuario}", size=20),
            ft.Row([
                ft.ElevatedButton("Salir", icon="logout", icon_color="red", color="red", bgcolor="TRANSPARENT" ,on_click=lambda _: cerrar_app(page)),
            ]),
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.START,
        ), # Menú lateral
        ft.Row([
            ft.Container(
                ft.Text("Test 1", size=30),
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