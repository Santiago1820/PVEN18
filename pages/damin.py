# importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.mvc import *
from models.pages import *
from models.query import *
from config.settings import *
from sources.menu import *

# Función para obtener la altura de la pantalla
def screeny(window_height):
    return window_height

# Codigo de la funcion RegisterPage
def Dadmin(page: ft.Page):
    page.clean()
    if is_logged(page) is not False:
        if is_admin(page) is True:
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
                        ft.Container(
                            content=ft.Image(
                                src=f"{logo}",
                                width=200,
                                height=200,
                            ),
                            **card_style,
                        ),
                        ft.Text(f"Menú administrativo", style=ft.TextStyle(size=40, weight=ft.FontWeight.BOLD)),
                        ft.Container(
                            content=ft.Row([
                                ft.Column([
                                    ft.Container(
                                        content=ft.Row([ft.Icon(ft.icons.PEOPLE, color="white"), ft.Text("Clientes")], alignment=ft.MainAxisAlignment.CENTER),
                                        alignment=ft.alignment.center,
                                        padding=10,
                                        margin=ft.margin.only(bottom=45),
                                        ink=True,
                                        on_click=lambda _: page.go("/admin/clients")
                                    ),
                                    ft.Container(
                                        content=ft.Row([ft.Icon(ft.icons.SUPERVISED_USER_CIRCLE, color="green"), ft.Text("Usuarios")], alignment=ft.MainAxisAlignment.CENTER),
                                        alignment=ft.alignment.center,
                                        padding=10,
                                        margin=ft.margin.only(bottom=45),
                                        ink=True,
                                        on_click=lambda _: page.go("/admin/users")
                                    ),
                                ], height=400, width=200, alignment=ft.MainAxisAlignment.CENTER),
                                ft.Column([
                                    ft.Container(
                                        content=ft.Row([ft.Icon(ft.icons.NOTE_ALT, color="yellow"), ft.Text("Proyectos")], alignment=ft.MainAxisAlignment.CENTER),
                                        alignment=ft.alignment.center,
                                        padding=10,
                                        margin=ft.margin.only(bottom=45),
                                        ink=True,
                                        on_click=lambda _: page.go("/admin/projects")
                                    ),
                                    ft.Container(
                                        content=ft.Row([ft.Icon(ft.icons.WORKSPACE_PREMIUM, color="blue"), ft.Text("Tareas")], alignment=ft.MainAxisAlignment.CENTER),
                                        alignment=ft.alignment.center,
                                        padding=10,
                                        margin=ft.margin.only(bottom=45),
                                        ink=True,
                                        on_click=lambda _: page.go("/admin/tasks")
                                    ),
                                ], width=200, alignment=ft.MainAxisAlignment.CENTER),
                                ft.Column([
                                    ft.Container(
                                        content=ft.Row([ft.Icon(ft.icons.WORKSPACES, color="#f9a640"), ft.Text("Campañas")], alignment=ft.MainAxisAlignment.CENTER),
                                        alignment=ft.alignment.center,
                                        padding=10,
                                        margin=ft.margin.only(bottom=45),
                                        ink=True,
                                        on_click=lambda _: page.go("/admin/campaigns")
                                    ),
                                    ft.Container(
                                        content=ft.Row([ft.Icon(ft.icons.SETTINGS, color="white"), ft.Text("Configuración")], alignment=ft.MainAxisAlignment.CENTER),
                                        alignment=ft.alignment.center,
                                        padding=10,
                                        margin=ft.margin.only(bottom=45),
                                        ink=True,
                                        on_click=lambda _: page.go("/admin/settings")
                                    ),
                                ], width=200, alignment=ft.MainAxisAlignment.CENTER)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            bgcolor=ft.colors.SURFACE,
                            height=300,
                            border_radius=10,
                            padding=20,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=10,
                                color=ft.colors.with_opacity(0.3, ft.colors.BLACK),
                            ),
                        ),
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