# Importar las librerías necesarias
import flet as ft
import re

# Variable para corregir error de doble apertura
window_closed = False

# Importar las funciones necesarias
from models.pages import *
from config.settings import titulo, tema, logo
from models.mvc import *

# Función para cerrar la aplicación
def cerrar_app(e):
    e.page.window.close()

# Función para manejar el evento de clic en el botón "Entrar"
def entrar_click(e):
    user = username.value
    contra = password.value
    e.page.update()

    # Validamos los campos que no sean vacios
    if user == "" or contra == "":
        open_error_campo(e)
        return
    
    # Validamos el formato del correo
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user):
        open_error_correo(e)
        return
    
    # Encriptamos la contraseña
    password_hash = encriptar(contra)

    # Validamos el usuario que sea valido y lo comparamos si es administrador o si es usuario
    usuario_valido = validar_usuario(user, password_hash)
    if usuario_valido is None:
        open_error_user(e)
        return
    elif usuario_valido[0] == "Administrativo":
        e.page.go("/admin")
    else:
        e.page.go("/dashboard")
        return

# Función para abrir el mensaje de error de validación de campos
def open_error_campo(e):
    e.page.overlay.append(error_campo)
    error_campo.open = True
    e.page.update()

# Función para cerrar el mensaje de error de validación de campos
def close_error_campo(e):
    error_campo.open = False
    e.page.update()

# Función para abrir el mensaje de error de usuario o contraseña incorrectos
def open_error_user(e):
    e.page.overlay.append(error_user)
    error_user.open = True
    e.page.update()

# Función para cerrar el mensaje de error de usuario o contraseña incorrectos
def close_error_user(e):
    error_user.open = False
    e.page.update()

# Función para abrir el mensaje de error de correo
def open_error_correo(e):
    e.page.overlay.append(error_correo)
    error_correo.open = True
    e.page.update()

# Función para cerrar el mensaje de error de correo
def close_error_correo(e):
    error_correo.open = False
    e.page.update()

# Mensaje de error de validación de campos
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

# Mensaje de error de usuario o contraseña incorrectos
error_user = ft.AlertDialog(
    modal=True,
    title=ft.Text("Error"),
    content=ft.Text("Correo o contraseña incorrectos"),
    actions=[
        ft.TextButton(
            "Cerrar",
            on_click=close_error_user,
        ),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
)

# Mensaje de error de correo
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

# Código que manda a llamar a la página de LoginPage
def LoginPage(page: ft.Page):
    # Función para corregir error de doble apertura (Para ejecutarlo en editor de codigo comenta las lineas 125-128 si lo vas a correr desde un archivo empaquetado descomentarla)
    # global window_closed
    # if not window_closed:
    #     page.window.close()
    #     window_closed = True

    # Función para bloquear el login en dado caso de que ya haya iniciado sesión (Únicamente en web) 
    if login_block(page) is not True:

        # Definir las propiedades de la página
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
        page.adaptive = True

        # Definimos los campos de usuario, contraseña y tipo de usuario
        global username, password
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

        # Barra de título personalizada la cual evita el movimiento de la ventana y tiene icono de "x" para poder salir del programa
        page.add(
            ft.Container(
                ft.Container(ft.IconButton(ft.icons.CLOSE, on_click=cerrar_app, icon_color='red', tooltip='Cerrar'), height=30, alignment=ft.alignment.center_right)
            )
        )

        # Código de la página de inicio de sesión
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
                                        ), padding=ft.padding.only(120, 0),
                                    ),
                                    ft.Text(
                                        "Iniciar Sesión",
                                        color="black",
                                        size=30,
                                        weight='w700',
                                        width=360,
                                        text_align="center",
                                    ),
                                    ft.Text(
                                        "Por favor inicie sesión para continuar",
                                        color="#2e526d",
                                        width=360,
                                        text_align="center",
                                    ),
                                    ft.Container(
                                        username, padding=ft.padding.only(40, 20),
                                    ),
                                    ft.Container(
                                        password, padding=ft.padding.only(40, 20),
                                    ),
                                    ft.Container(
                                        ft.TextButton(
                                            content=ft.Text("¡Olvidé mi contraseña!",
                                                            color="#303030",
                                                            weight='w500',), on_click=lambda _: page.go("/forgot"),
                                        ), padding=ft.padding.only(40),
                                    ),
                                    ft.Container(
                                        ft.ElevatedButton(
                                            content=ft.Text(
                                                "Entrar",
                                                color='white',
                                                weight='w500',
                                            ), width=280, bgcolor='black',
                                            on_click=entrar_click,
                                        ), padding=ft.padding.only(40, 10),
                                    ),
                                    ft.Container(
                                        ft.Row([
                                            ft.Text(
                                                "¿No tienes una cuenta?",
                                                color="#303030",
                                            ),
                                            ft.TextButton(
                                                on_click=lambda _: page.go("/register"),
                                                content=ft.Text("Regístrate", color="#303030",),
                                            )
                                        ], spacing=-1), padding=ft.padding.only(40),
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
