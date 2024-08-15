import os
import flet as ft
import webbrowser

# Importar las funciones necesarias
from fpdf import FPDF
from models.pages import *
from config.settings import *
from models.mvc import *
from models.query import *
from sources.menu import *

# Función para obtener la altura de la pantalla
def screeny(window_height):
    return window_height    

# Código de la función Reports
def Reports(page: ft.Page):
    page.clean()
    page.update()

    def pendiente():
        # Ruta donde se guardará el PDF
        ruta_directorio = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        nombre_archivo = f"{iuser[0]}_Tareas_Pendientes.pdf"
        ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)

        # Crear el documento PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Agregar título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Tareas Pendientes", ln=True, align='C')
        
        # Agregar contenido de tareas pendientes
        pdf.set_font("Arial", size=12)
        for tarea in pendientes:
            pdf.cell(200, 10, txt=f"{tarea[0]} | Vencimiento: {tarea[1].strftime('%d-%m-%Y')}", ln=True)
        
        # Guardar el archivo
        pdf.output(ruta_archivo)
        
        # Abrir la carpeta donde se guardó el archivo
        if os.name == 'nt':  # Para Windows
            os.startfile(ruta_directorio)
        elif os.name == 'posix':  # Para Unix (Linux y Mac)
            webbrowser.open(f"file://{os.path.abspath(ruta_directorio)}")

    def en_progreso():
        # Ruta donde se guardará el PDF
        ruta_directorio = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        nombre_archivo = f"{iuser[0]}_Tareas_En_Progreso.pdf"
        ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)

        # Crear el documento PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Agregar título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Tareas En Progreso", ln=True, align='C')
        
        # Agregar contenido de tareas pendientes
        pdf.set_font("Arial", size=12)
        for tarea in progresos:
            pdf.cell(200, 10, txt=f"{tarea[0]} | Vencimiento: {tarea[1].strftime('%d-%m-%Y')}", ln=True)
        
        # Guardar el archivo
        pdf.output(ruta_archivo)
        
        # Abrir la carpeta donde se guardó el archivo
        if os.name == 'nt':  # Para Windows
            os.startfile(ruta_directorio)
        elif os.name == 'posix':  # Para Unix (Linux y Mac)
            webbrowser.open(f"file://{os.path.abspath(ruta_directorio)}")

    def terminada():
        # Ruta donde se guardará el PDF
        ruta_directorio = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        nombre_archivo = f"{iuser[0]}_Tareas_Completa.pdf"
        ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)

        # Crear el documento PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Agregar título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Tareas En Progreso", ln=True, align='C')
        
        # Agregar contenido de tareas pendientes
        pdf.set_font("Arial", size=12)
        for tarea in terminados:
            pdf.cell(200, 10, txt=f"{tarea[0]}", ln=True)
        
        # Guardar el archivo
        pdf.output(ruta_archivo)
        
        # Abrir la carpeta donde se guardó el archivo
        if os.name == 'nt':  # Para Windows
            os.startfile(ruta_directorio)
        elif os.name == 'posix':  # Para Unix (Linux y Mac)
            webbrowser.open(f"file://{os.path.abspath(ruta_directorio)}")

    page.clean()
    page.update()
    if is_logged(page) is not False:
        iuser = nombre_usuario()[0]
        pendientes = tareas_pendientes()
        progresos = tareas_progreso()
        terminados = tareas_terminadas()
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
            "padding": 10,
            "shadow": ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.3, ft.colors.BLACK),
            )
        }

        # Obtener altura de la pantalla y ajustar el tamaño de todos los contenedores de tablas
        contenedor_alto = screeny(page.window.height)

        # Crear las tablas con el mismo tamaño
        tabla_pendientes = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            columns=[
                ft.DataColumn(ft.Text("Pendientes:", style=title_style)),
                ft.DataColumn(ft.Container(
                    content= ft.Row([ft.Text("Exportar", color="White", weight=ft.FontWeight.BOLD), ft.Icon(ft.icons.PICTURE_AS_PDF, color="red"),]),
                    padding=10,
                    margin=ft.margin.only(top=20),
                    ink=True,
                    on_click=lambda _: pendiente(),
                )),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(f"{pendiente[0]} | Vencimiento: {pendiente[1].strftime('%d-%m-%Y')}")),
                    ft.DataCell(ft.Text("")),
                ]) for pendiente in pendientes
            ],
        )
        tabla_progresos = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            data_row_color={ft.MaterialState.HOVERED: ft.colors.SECONDARY_CONTAINER},
            columns=[
                ft.DataColumn(ft.Text("Progreso:", style=title_style)),
                ft.DataColumn(ft.Container(
                    content= ft.Row([ft.Text("Exportar", color="White", weight=ft.FontWeight.BOLD), ft.Icon(ft.icons.PICTURE_AS_PDF, color="red"),]),
                    padding=10,
                    margin=ft.margin.only(top=20),
                    ink=True,
                    on_click=lambda _: en_progreso(),
                )),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(f"{progreso[0]} | Vencimiento: {progreso[1].strftime('%Y-%m-%d')}")),
                    ft.DataCell(ft.Text("")),
                ]) for progreso in progresos
            ],
        )
        tabla_terminadas = ft.DataTable(
            bgcolor=ft.colors.SURFACE,
            heading_row_color=ft.colors.SECONDARY_CONTAINER,
            heading_row_height=70,
            data_row_color={ft.MaterialState.HOVERED: ft.colors.SECONDARY_CONTAINER},
            columns=[
                ft.DataColumn(ft.Text("Completa:", style=title_style)),
                ft.DataColumn(ft.Container(
                    content= ft.Row([ft.Text("Exportar", color="White", weight=ft.FontWeight.BOLD), ft.Icon(ft.icons.PICTURE_AS_PDF, color="red"),]),
                    padding=10,
                    margin=ft.margin.only(top=20),
                    ink=True,
                    on_click=lambda _: terminada(),
                )),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(f"{Completa[0]}")),
                    ft.DataCell(ft.Text("")),
                ]) for Completa in terminados
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
                                            controls=[tabla_pendientes],
                                            expand=True,
                                        ),
                                        **card_style,
                                        width=400,
                                        height=contenedor_alto,  
                                    ),
                                    ft.Container(
                                        content=ft.ListView( 
                                            controls=[tabla_progresos],
                                            expand=True,
                                        ),
                                        **card_style,
                                        width=400,
                                        height=contenedor_alto,  
                                    ),
                                    ft.Container(
                                        content=ft.ListView( 
                                            controls=[tabla_terminadas],
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