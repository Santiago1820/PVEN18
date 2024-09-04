import flet as ft
from models.pages import *
from config.settings import titulo, tema
from models.mvc import *

def Error404(page: ft.Page):
    page.clean()
    page.update()
    page.title = titulo
    page.theme_mode = tema
    
    # Crear el texto de la página 404
    not_found_text = ft.Text("404 - Página no encontrada")
    
    # Crear el botón para regresar a la ruta anterior
    back_button = ft.ElevatedButton(
        text="Ir atrás",
        on_click=lambda e: go_back(page)
    )
    
    # Agregar los elementos a la página
    page.add(ft.SafeArea(not_found_text))
    page.add(ft.SafeArea(back_button))
    page.update()