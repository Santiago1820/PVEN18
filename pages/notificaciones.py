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

# Código de la función Notifications
def Notifications(page: ft.Page):
    page.clean()
    page.update()

    def leida(notificacion):
        pass

    def borrar(notificacion):
        pass

    page.clean()
    page.update()
    if is_logged(page) is not False:
        notis = notificaciones_sin_leer()
        nots = notificaciones_leidas()
        page.window_title_bar_hidden = False
        page.window_maximized = True
        page.title = titulo
        page.theme_mode = tema
        page.bgcolor = ft.colors.SURFACE_VARIANT
        page.padding = 0

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
        contenedor_alto = screeny(page.window_height)

        # Crear las tablas con el mismo tamaño
        tabla_not = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            columns=[
                ft.DataColumn(ft.Text("Notificaciones:", style=title_style)),
                ft.DataColumn(ft.Text("Acción")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(f"{noti[6]} | Vencimiento: {noti[3].strftime('%Y-%m-%d')}"), on_tap=lambda e, n=noti[0]: leida(n)),
                    ft.DataCell(ft.ElevatedButton("Leída", 
                                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), color="#b3efc8"),
                                                  on_click=lambda e, n=noti[0]: leida(n))),
                ]) for noti in notis
            ],
        )
        tabla_not_leidas = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            data_row_color={ft.MaterialState.HOVERED: ft.colors.SECONDARY_CONTAINER},
            columns=[
                ft.DataColumn(ft.Text("Leídas:", style=title_style)),
                ft.DataColumn(ft.Text("Acción")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(notss[6])),
                    ft.DataCell(ft.ElevatedButton("Borrar", 
                                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), color="red"),
                                                  on_click=lambda e, n=notss[0]: borrar(n))),
                ]) for notss in nots
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
                                            controls=[tabla_not],
                                            expand=True,
                                        ),
                                        **card_style,
                                        width=800,
                                        height=contenedor_alto,  
                                    ),
                                    ft.Container(
                                        content=ft.ListView( 
                                            controls=[tabla_not_leidas],
                                            expand=True,
                                        ),
                                        **card_style,
                                        width=400,
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