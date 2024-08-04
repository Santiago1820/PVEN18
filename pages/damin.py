# importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.pages import *
from config.settings import titulo, tema, logo

# Codigo de la funcion RegisterPage
def Dadmin(page: ft.Page):
    # Definir las propiedades de la pagina
    page.window_title_bar_hidden = True
    page.window_width = 580
    page.window_height = 740
    page.title = titulo
    page.theme_mode = tema
    page.padding = 0
    # Barra de titulo personalizada
    page.add(
        ft.Container(
            ft.Container(ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close(), icon_color='red', tooltip='Cerrar'),height=30, alignment=ft.alignment.center_right)
        )
    )
    # Codigo de la pagina de registro
    page.add(
        ft.Text("Dashboard Admin")
        )