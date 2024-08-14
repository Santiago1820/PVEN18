# Importar las librerias necesarias
import flet as ft
import re

# importar las funciones necesarias
from models.pages import *
from config.settings import titulo, tema, logo
from models.mvc import *
from models.query import *

# Codigo de la funcion RegisterPage
def RegisterPage(page: ft.Page):
    if login_block(page) is not True:
        # Definir las propiedades de la pagina
        page.window_width = 580
        page.window_title_bar_hidden = True
        page.window_maximized = False
        page.window_height = 740
        page.title = titulo
        page.theme_mode = tema
        page.bgcolor = ft.colors.SURFACE_VARIANT
        page.padding = 0
        page.window_top = screeny(page.window_height)
        page.window_left = screenx(page.window_width)

        # Definimos los campos de nombre, correo y contraseña
        nombre = ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='Nombre',
                                    border='underline',
                                    color="#303030",
                                    prefix_icon=ft.icons.EDIT,
                                )
        username = ft.TextField(
                                    width=280,
                                    height=40,
                                    hint_text='Correo',
                                    border='underline',
                                    color="#303030",
                                    prefix_icon=ft.icons.EMAIL,
                                )
        password = ft.TextField(
                                    can_reveal_password=True,
                                    width=280,
                                    height=40,
                                    hint_text='Contraseña',
                                    border='underline',
                                    color="#303030",
                                    prefix_icon=ft.icons.LOCK,
                                    password=True,
                                )

        # Mensaje de error de validacion de campos
        def open_error_campo(e):
            page.dialog = error_campo 
            error_campo.open = True
            page.update()

        def close_error_campo(e):
            page.dialog = error_campo 
            error_campo.open = False
            page.update()

        error_campo = ft.CupertinoAlertDialog(
            title=ft.Text("Error"),
            content=ft.Text("Por favor llene todos los campos"),
            actions=[
                ft.CupertinoDialogAction(
                    "Cerrar",
                    is_destructive_action=True,
                    on_click=close_error_campo,
                ),
            ],
        )

        def open_error_user(e):
            page.dialog = error_user
            error_user.open = True
            page.update()

        def close_error_user(e):
            page.dialog = error_user 
            error_user.open = False
            page.update()

        error_user = ft.CupertinoAlertDialog(
            title=ft.Text("Error"),
            content=ft.Text("Correo ya registrado"),
            actions=[
                ft.CupertinoDialogAction(
                    "Cerrar",
                    is_destructive_action=True,
                    on_click=close_error_user,
                ),
            ],
        )

        def open_error_correo(e):
            page.dialog = error_correo
            error_correo.open = True
            page.update()

        def close_error_correo(e):
            page.dialog = error_correo 
            error_correo.open = False
            page.update()
        error_correo = ft.CupertinoAlertDialog(
            title=ft.Text("Error"),
            content=ft.Text("Solo se permiten correos"),
            actions=[
                ft.CupertinoDialogAction(
                    "Cerrar",
                    is_destructive_action=True,
                    on_click=close_error_correo,
                ),
            ],
        )

        # Definimos la funcion para el boton de entrar
        def entrar_click(e):
            name = nombre.value
            user = username.value
            contra = password.value
            page.update()

            # Validamos los campos
            if user == "" or contra == "" or name == "":
                open_error_campo(e)
                return
            
            # Validamos el formato del correo
            if not re.match(r"[^@]+@[^@]+\.[^@]+", user):
                open_error_correo(e)
                return
            
            # Encriptamos la contraseña
            password_hash = encriptar(contra)

            # Validamos el usuario
            usuario_valido = is_registered(user)
            if usuario_valido != []:
                open_error_user(e)
                return
            else:
                registrar_usuario(name, user, password_hash)
                page.go("/")
                return
            


        # Barra de titulo personalizada
        page.add(
            ft.Container(
                ft.Container(ft.IconButton(ft.icons.CLOSE, on_click=lambda _: cerrar_app(page), icon_color='red', tooltip='Cerrar'),height=30, alignment=ft.alignment.center_right)
            )
        )
        # Codigo de la pagina de inicio de sesion
        page.add(
            ft.Container(
                ft.Container(
                    ft.Stack([
                        ft.Container(
                            border_radius=11,
                            rotate=ft.Rotate(0.98*3.14),
                            width=360,
                            height=560,
                            bgcolor="#686868",
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
                                "Crear Cuenta",
                                color="black",
                                size=30,
                                weight='w700',
                                width=360,
                                text_align="center",
                            ),
                            ft.Text(
                                "Registrate con tus datos personales",
                                color="#2e526d",
                                width=360,
                                text_align="center",
                            ),
                            ft.Container(
                                nombre,padding=ft.padding.only(40,20),
                            ),
                            ft.Container(
                                username,padding=ft.padding.only(40,20),
                            ),
                            ft.Container(
                            password,padding=ft.padding.only(40,20),
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content= ft.Text(
                                            "Registrate", 
                                            color='white',
                                            weight='w500', 
                                    ),width=280, bgcolor='black',
                                    on_click=entrar_click,
                                ),padding=ft.padding.only(40,10),
                            ),
                            ft.Container(
                                ft.Row([
                                    ft.Text(
                                        "¿Tienes una cuenta?",
                                        color="#303030",
                                    ),
                                    ft.TextButton(
                                        on_click=lambda _: page.go("/"),
                                        content= ft.Text("Iniciar sesión",color="#303030",),
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