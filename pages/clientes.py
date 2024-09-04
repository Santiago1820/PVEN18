import flet as ft
import datetime

# Importar las funciones necesarias
from models.pages import *
from config.settings import *
from models.mvc import *
from models.query import *
from sources.menu import *

# Función para obtener la altura de la pantalla
def screeny(window_height):
    return window_height

# Código de la función Clients
def Clients(page: ft.Page):
    page.clean()
    page.update()

    def ver_mas_cliente(cliente):
        pass


    page.clean()
    page.update()
    if is_logged(page) is not False:
        clientes = clientes_usuario()
        page.window.title_bar_hidden = False
        page.window.maximized = True
        page.title = titulo
        page.theme_mode = tema
        page.bgcolor = ft.colors.SURFACE_VARIANT
        page.padding = 0
        page.adaptive = True

        # Estilos de el título y las tarjetass
        title_style = ft.TextStyle(size=24, weight=ft.FontWeight.BOLD)
        card_style = {
            "bgcolor": ft.colors.SURFACE,
            "padding": 20,
            "shadow": ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.3, ft.colors.BLACK),
            )
        }

        # Obtener altura de la pantalla y ajustar el tamaño de todos los contenedores de tablas
        contenedor_alto = screeny(page.window.height)

        # Crear las tablas con el mismo tamaño
        tabla_clientes = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            columns=[
                ft.DataColumn(ft.Text("Clientes:", style=title_style)),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(f"{cliente[1]}"), on_tap=lambda e, c=cliente[0]: ver_mas_cliente(c)),
                ]) for cliente in clientes
            ],
        )

        # Agregar menú lateral
        menu_lateral = menu(page)

        page.add(
            ft.ListView(
                controls=[
                    ft.Row([
                        # Menú lateral estilos
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
                        # Mostramos las tablas
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Container(
                                        content=ft.ListView( 
                                            controls=[tabla_clientes],
                                            expand=True,
                                        ),
                                        **card_style,
                                        width=800,
                                        height=contenedor_alto,  
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                ),
                            ],
                            spacing=30,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            expand=True,
                            padding=20,
                        ),
                    ],
                    expand=True,
                    ),
                ],
                expand=True,
            )
        )
    page.update()