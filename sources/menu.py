# importamos las librerias necesarias
import flet as ft

from models.mvc import *
from models.query import *

def menu(page):
            is_ad = tipo_usuario()[0]
            if is_ad[0] == "Administrativo":
                admin_menu = ft.Column([
                    ft.ElevatedButton("Administración", icon="admin_panel_settings", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/admin")),
                    ft.ElevatedButton("Inicio", icon="home", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/dashboard")),
                    ft.ElevatedButton("Perfil", icon="person", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/me")),
                    ft.ElevatedButton("Clientes", icon="emoji_people", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/clients")),
                    ft.ElevatedButton("Reportes", icon="file_open", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/reports")),
                    ft.ElevatedButton("Salir", icon="logout", icon_color="red", color="red", bgcolor="TRANSPARENT" ,on_click=lambda _: cerrar_sesion(page)),
                ])
                return admin_menu
            else:
                menu_user = ft.Column([
                    ft.ElevatedButton("Inicio", icon="home", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/dashboard")),
                    ft.ElevatedButton("Perfil", icon="person", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/me")),
                    ft.ElevatedButton("Clientes", icon="emoji_people", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/clients")),
                    ft.ElevatedButton("Reportes", icon="file_open", icon_color="white", color="white", bgcolor="TRANSPARENT" ,on_click=lambda _: page.go("/reports")),
                    ft.ElevatedButton("Salir", icon="logout", icon_color="red", color="red", bgcolor="TRANSPARENT" ,on_click=lambda _: cerrar_sesion(page)),          
                ])
                return menu_user