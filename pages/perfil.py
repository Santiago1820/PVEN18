# Importar las librerías necesarias
import flet as ft

# Importar las funciones necesarias
from models.pages import *
from config.settings import *
from models.mvc import *
from models.query import *
from sources.menu import *

# Código de la función Profile
def Profile(page: ft.Page):
    page.clean()
    page.update()
    if is_logged(page) is not False:
        nombre = nombre_usuario()[0]
        correo = correo_usuario()[0]
        contraseña = contraseña_usuario()[0]
        imagen = imagen_usuario()[0]
        
        # Definir las propiedades de la página
        page.window.title_bar_hidden = False
        page.window.maximized = True
        page.title = titulo
        page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = ft.colors.SURFACE_VARIANT
        page.padding = 0

        # Estilos comunes
        title_style = ft.TextStyle(size=30, weight=ft.FontWeight.BOLD)
        card_style = {
            "bgcolor": "#a5a5a5",
            "border_radius": 10,
            "padding": 20,
            "shadow": ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.3, ft.colors.BLACK),
            )
        }

        # Menú lateral
        menu_lateral = menu(page)

        # Estructura de la página
        page.add(ft.Row([
            # Columna del Menú lateral
            ft.Container(
                content=ft.Column(
                    [ft.Text(f"{nombre_app}", style=title_style)] + menu_lateral.controls,
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                width=250,
                bgcolor=ft.colors.SURFACE,
                padding=20,
                height=page.height,
            ),
            # Contenido principal
            ft.Container(
                content=ft.Column([
                    ft.Text("Mi perfil", style=ft.TextStyle(size=40, weight=ft.FontWeight.BOLD)),
                    ft.Container(
                        content=ft.Image(
                            src=obtener_img_usr(imagen[0]),
                            width=200,
                            height=200,
                        ),
                        **card_style,
                    ),
                    ft.Text(f"Nombre: {nombre[0]}", size=20),
                    ft.Text(f"Correo Electrónico: {correo[0]}", size=20),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True,
                padding=20,
            ),
        ],
        expand=True,
        ))
    page.update()
