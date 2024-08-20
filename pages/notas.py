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

# Código de la función Notes
def Notes(page: ft.Page):
    page.clean()
    def ver_mas_proyecto_info():
        pass
    def ver_mas_proyecto(proyecto):
        id_proyecto_usuario(proyecto)
        guardar_id_proyecto()[0]
        actualizar_tabla_tareas()
        page.update()

    def actualizar_tabla_tareas():
        tareas = tareas_usuario()
        tabla_tareas.rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(tarea[0]),),
                ft.DataCell(ft.ElevatedButton("Seleccionar", 
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),color="#f7ee8a"),
                                              on_click=lambda e, t=tarea: ver_mas_tarea(t))),
            ]) for tarea in tareas
        ]

    def ver_mas_tarea(tarea):
        id_tarea_usuario(tarea[0])
        guardar_id_tarea()
        actualizar_tabla_info()
        info_tarea()
        page.update()

    def actualizar_tabla_info():
        infos = info_tarea()
        proyecto = nombre_proyecto()[0]
        tabla_infos.rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Container(
                ft.Column([
                    ft.Text("Proyecto:", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(proyecto[0]),
                    ft.Text("Tarea:", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(info[1]),
                    ft.Text("Descripción:", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(info[2]),
                    ft.Text("Fecha inicio:", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(datetime.datetime.fromisoformat(str(info[3])).strftime('%d/%m/%y')),
                    ft.Text("Fecha fin:", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(datetime.datetime.fromisoformat(str(info[4])).strftime('%d/%m/%y')),
                    ft.Text("Estado:", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(info[5]),
                    ft.Text("Prioridad:", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(info[6]),
                ]),
                ),
                    ),
            ]) for info in infos
        ]

    page.clean()
    page.update()
    if is_logged(page) is not False:
        proyectos = proyectos_usuario()
        page.window.title_bar_hidden = False
        page.window.maximized = True
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
        contenedor_alto = screeny(page.window.height)

        # Crear las tablas con el mismo tamaño
        tabla_proyectos = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            columns=[
                ft.DataColumn(ft.Text("Proyectos", style=title_style)),
                ft.DataColumn(ft.Text("Acción")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(proyecto[0]), on_tap=lambda e, p=proyecto: ver_mas_proyecto_info()),
                    ft.DataCell(ft.ElevatedButton("Seleccionar", 
                                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), color="#b3efc8"),
                                                  on_click=lambda e, p=proyecto[0]: ver_mas_proyecto(p))),
                ]) for proyecto in proyectos
            ],
        )

        tabla_tareas = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            data_row_color={ft.MaterialState.HOVERED: ft.colors.SECONDARY_CONTAINER},
            columns=[
                ft.DataColumn(ft.Text("Tareas", style=title_style)),
                ft.DataColumn(ft.Text("Acción")),
            ],
            rows=[],
        )

        tabla_infos = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            columns=[
                ft.DataColumn(ft.Text("Información", style=title_style)),
            ],
            rows=[],
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
                                            controls=[tabla_proyectos],
                                            expand=True,
                                        ),
                                        **card_style,
                                        width=400,
                                        height=contenedor_alto,  
                                    ),
                                    ft.Container(
                                        content=ft.ListView( 
                                            controls=[tabla_tareas],
                                            expand=True,
                                        ),
                                        **card_style,
                                        width=400,
                                        height=contenedor_alto,  
                                    ),
                                    ft.Container(
                                        content=ft.ListView( 
                                            controls=[tabla_infos],
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