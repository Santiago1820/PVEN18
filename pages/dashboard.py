# importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.pages import *
from config.settings import *
from models.mvc import *
from models.query import *
from sources.menu import *

# Codigo de la funcion RegisterPage
def Dashboard(page: ft.Page):
    def ver_mas_proyecto(proyecto):
        id_proyecto_usuario(proyecto)
        guardar_id_proyecto()[0]
        actualizar_tabla_tareas()
        page.update()
    
    def actualizar_tabla_tareas():
        tareas = tareas_usuario()
        tabla_tareas.rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(tarea[0])),
                ft.DataCell(ft.ElevatedButton("Seleccionar", on_click=lambda e, t=tarea: ver_mas_tarea(t))),
            ]) for tarea in tareas
        ]

    def ver_mas_tarea(tarea):
        pass

    page.clean()
    page.update()
    if is_logged(page) is not False: 
        proyectos = proyectos_usuario()
        # tareas = tareas_usuario()
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
                    ft.Text(f"Dashboard", size=40),
                    ft.Row([
                        ft.Column([
                        tabla_proyectos := ft.DataTable(
                            border=ft.border.all(2, "gray"),
                            border_radius=10,
                            vertical_lines=ft.BorderSide(3, "gray"),
                            horizontal_lines=ft.BorderSide(3, "gray"),
                            columns=[
                                ft.DataColumn(ft.Text("Proyectos:", size=20)),
                                ft.DataColumn(ft.Text("")),
                            ],
                            rows=[
                                ft.DataRow(cells=[
                                    ft.DataCell(ft.Text(proyecto[0])),
                                    ft.DataCell(ft.ElevatedButton("Seleccionar", on_click=lambda e, p=proyecto[0]: ver_mas_proyecto(p))),
                                ]) for proyecto in proyectos
                            ],
                        ), # Proyectos de el usuario
                        ]), # Proyectos
                        ft.Column([
                        tabla_tareas := ft.DataTable(
                            border=ft.border.all(2, "gray"),
                            border_radius=10,
                            vertical_lines=ft.BorderSide(3, "gray"),
                            horizontal_lines=ft.BorderSide(3, "gray"),
                            columns=[
                                ft.DataColumn(ft.Text("Tareas:", size=20)),
                                ft.DataColumn(ft.Text("")),
                            ],
                            rows=[],
                        ), # Proyectos de el usuario
                        ]), # Tareas
                        ft.Column([
                        ft.Text(f"Información:", size=20),
                        ]), # Informacion
                    ]),
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

