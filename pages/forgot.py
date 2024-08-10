# importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.mvc import *
from models.pages import *
from config.settings import titulo, tema, logo

# Codigo de la funcion RegisterPage
def ForgotPage(page: ft.Page):
    page.clean()
    page.update()
    if login_block(page) is not True:
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
            ft.Container(
                ft.Container(
                    ft.Stack([
                        ft.Container(
                            border_radius=11,
                            rotate=ft.Rotate(0.98*3.14),
                            width=360,
                            height=560,
                            bgcolor="#22ffffff",
                        ),
                ft.Container(
                    ft.Container(
                        ft.Column([
                            ft.Container(
                                ft.Image(
                                    src=logo,
                                    width=100,
                                ),padding=ft.padding.only(120,0),
                            ),
                            ft.Text(
                                "Recuperar Contraseña",
                                size=25,
                                weight='w700',
                                width=360,
                                text_align="center",
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='Correo administrador',
                                    border='underline',
                                    color="#303030",
                                    prefix_icon=ft.icons.EMAIL,
                                ),padding=ft.padding.only(40,20),
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='Contraseña administrador',
                                    border='underline',
                                    color="#303030",
                                    prefix_icon=ft.icons.LOCK,
                                    can_reveal_password=True,
                                    password=True,
                                ),padding=ft.padding.only(40,20),
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='Correo Operativo',
                                    border='underline',
                                    color="#303030",
                                    prefix_icon=ft.icons.EMAIL,
                                ),padding=ft.padding.only(40,20),
                            ),
                            ft.Container(
                                ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='Nueva Contraseña',
                                    border='underline',
                                    color="#303030",
                                    prefix_icon=ft.icons.LOCK,
                                    can_reveal_password=True,
                                    password=True,
                                ),padding=ft.padding.only(40,20),
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content= ft.Text(
                                            "Actualizar", 
                                            color='white',
                                            weight='w500', 
                                    ),width=280, bgcolor='black', 
                                ),padding=ft.padding.only(40,10),
                            ),
                            ft.Container(
                                ft.Row([
                                    ft.TextButton(
                                        on_click=lambda _: page.go("/"),
                                        content= ft.Text("Volver al inicio",color="#303030",),
                                    )
                                ],spacing=-1),padding=ft.padding.only(40),
                            )
                        ])
                    ),
                    width=360,
                    height=560,
                    bgcolor="#22ffffff",
                    border_radius=11,
                )
            ]),
            padding=110,
            width=360,
            height=560,
        ),
        width=580,
        height=740,
        gradient=ft.LinearGradient(['#09203f', '#537895']),
    )
        )
    page.update()