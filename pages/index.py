# Importar las librerias necesarias
import flet as ft

# importar las funciones necesarias
from models.pages import *
from config.settings import titulo, tema, logo
from models.mvc import *

# Codigo de la funcion LoginPage
def LoginPage(page: ft.Page):
    # Definir las propiedades de la pagina
    page.window_width = 580
    page.window_title_bar_hidden = True
    page.window_height = 740
    page.title = titulo
    page.theme_mode = tema
    page.padding = 0
    page.window_top = screeny(page.window_height)
    page.window_left = screenx(page.window_width)

    # Definimos los campos de usuario, contraseña y tipo de usuario
    username = ft.TextField(
                                width=280,
                                height=40,
                                hint_text='Usuario',
                                border='underline',
                                color="#303030",
                                prefix_icon=ft.icons.PERSON,
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
    
    tipo = ft.Dropdown(
        width=280,
        height=50,
        hint_text='Selecciona un tipo de usuario',
        text_size= 15,
        border_color= 'transparent',
        options =
        [
            ft.dropdown.Option("Operativo"),
            ft.dropdown.Option("Administrativo"),
        ]
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

    # Mensaje de error de usuario o contraseña incorrectos
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
        content=ft.Text("Usuario o contraseña incorrectos"),
        actions=[
            ft.CupertinoDialogAction(
                "Cerrar",
                is_destructive_action=True,
                on_click=close_error_user,
            ),
        ],
    )

    # Mensaje de error de permisos
    def open_error_permisos(e):
        page.dialog = error_permisos 
        error_permisos.open = True
        page.update()

    def close_error_permisos(e):
        page.dialog = error_permisos  
        error_permisos.open = False
        page.update()

    error_permisos  = ft.CupertinoAlertDialog(
        title=ft.Text("¡Upps!"),
        content=ft.Text("Parece que no eres un administrador"),
        actions=[
            ft.CupertinoDialogAction(
                "Cerrar",
                is_destructive_action=True,
                on_click=close_error_permisos,
            ),
        ],
    )

    # Definimos la funcion para el boton de entrar
    def entrar_click(e):
        global user
        user = username.value
        contra = password.value
        tipo_user = tipo.value
        page.update()

        # Validamos los campos
        if user == "" or contra == "" or tipo_user == "":
            open_error_campo(e)
            return
        
        # Encriptamos la contraseña
        password_hash = encriptar(contra)

        # Conectamos a la base de datos
        login(username.value, password_hash, tipo_user)


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
                            "Iniciar Sesión",
                            size=30,
                            weight='w700',
                            width=360,
                            text_align="center",
                        ),
                        ft.Text(
                            "Por favor inicie sesión para continuar",
                            width=360,
                            text_align="center",
                        ),
                        ft.Container(
                            username,padding=ft.padding.only(40,20),
                        ),
                        ft.Container(
                           password,padding=ft.padding.only(40,20),
                        ),
                        ft.Container(
                            tipo,padding=ft.padding.only(40,3),
                        ),
                        ft.Container(
                            ft.TextButton(
                                content= ft.Text("¡Olvidé mi contraseña!",
                                                 color="#303030",
                                                weight='w500',),
                            ),padding=ft.padding.only(40),
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                content= ft.Text(
                                        "Entrar", 
                                        color='white',
                                        weight='w500', 
                                ),width=280, bgcolor='black',
                                on_click=entrar_click,
                            ),padding=ft.padding.only(40,10),
                        ),
                        ft.Container(
                            ft.Row([
                                ft.Text(
                                    "¿No tienes una cuenta?",
                                    color="#303030",
                                ),
                                ft.TextButton(
                                    on_click=lambda _: page.go("/register"),
                                    content= ft.Text("Registrate",color="#303030",),
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
