# Importar las librerias necesarias
import flet as ft
import re

# Importar las funciones necesarias
from models.pages import *
from config.settings import titulo, tema, logo
from models.mvc import *
from models.query import *

# Codigo que manda a llamar a la página RegisterPage
def RegisterPage(page: ft.Page):

    # Validamos si el usuario esta logueado (Únicamente en web)
    if login_block(page) is not True:

        # Definir las propiedades de la pagina
        page.window.width = 580
        page.window.title_bar_hidden = True
        page.window.maximized = False
        page.window.height = 740
        page.title = titulo
        page.theme_mode = tema
        page.bgcolor = ft.colors.SURFACE_VARIANT
        page.padding = 0
        page.window.top = screeny(page.window.height)
        page.window.left = screenx(page.window.width)

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

        # Mensajes de errores (1. Abrir, 2. Cerrar, 3. Mensaje a mostrar)
        def open_error_campo(e):
            e.page.overlay.append(error_campo)
            error_campo.open = True
            e.page.update()

        def close_error_campo(e):
            error_campo.open = False
            e.page.update()

        error_campo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Error"),
            content=ft.Text("Por favor llene todos los campos"),
            actions=[
                ft.TextButton(
                    "Cerrar",
                    on_click=close_error_campo,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        def open_error_user(e):
            e.page.overlay.append(error_user)
            error_user.open = True
            e.page.update()

        def close_error_user(e):
            error_user.open = False
            e.page.update()

        error_user = ft.AlertDialog(
            modal= True,
            title=ft.Text("Error"),
            content=ft.Text("Correo ya registrado"),
            actions=[
                ft.TextButton(
                    "Cerrar",
                    on_click=close_error_user,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        def open_error_correo(e):
            e.page.overlay.append(error_correo)
            error_correo.open = True
            e.page.update()

        def close_error_correo(e):
            error_correo.open = False
            e.page.update()
        error_correo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Error"),
            content=ft.Text("Solo se permiten correos"),
            actions=[
                ft.TextButton(
                    "Cerrar",
                    on_click=close_error_correo,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        # Definimos la funcion para el boton de entrar
        def entrar_click(e):
            name = nombre.value
            user = username.value
            contra = password.value
            page.update()

            # Validamos los campos sean diferentes a nulos
            if user == "" or contra == "" or name == "":
                open_error_campo(e)
                return
            
            # Validamos el formato del correo
            if not re.match(r"[^@]+@[^@]+\.[^@]+", user):
                open_error_correo(e)
                return
            
            # Encriptamos la contraseña
            password_hash = encriptar(contra)

            # Validamos el usuario si esta registrado en dado caso de que este registrado le mostramos error, si no lo registramos y los redireccionamos a la página de inicio de sesión para que pueda iniciar sesión por primera vez
            usuario_valido = is_registered(user)
            if usuario_valido != []:
                open_error_user(e)
                return
            else:
                registrar_usuario(name, user, password_hash)
                page.go("/")
                return
            


        # Barra de titulo personalizada la cual evita el movimiento de la ventana, y agrega el botón "x" que manda a llamar la función para cerrar el programa
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