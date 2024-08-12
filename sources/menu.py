import flet as ft
from models.mvc import *
from models.query import *

def menu(page):
    is_ad = tipo_usuario()[0]

    # Menu usuario
    menu_items = [
        ft.Container(
            content=ft.Row([ft.Icon(ft.icons.HOME), ft.Text("Inicio")]),
            padding=10,
            margin=ft.margin.only(bottom=5),
            ink=True,
            on_click=lambda _: page.go("/dashboard")
        ),
        ft.Container(
            content=ft.Row([ft.Icon(ft.icons.PERSON), ft.Text("Perfil")]),
            padding=10,
            margin=ft.margin.only(bottom=5),
            ink=True,
            on_click=lambda _: page.go("/me")
        ),
        ft.Container(
            content=ft.Row([ft.Icon(ft.icons.PEOPLE), ft.Text("Clientes")]),
            padding=10,
            margin=ft.margin.only(bottom=5),
            ink=True,
            on_click=lambda _: page.go("/clients")
        ),
        ft.Container(
            content=ft.Row([ft.Icon(ft.icons.BAR_CHART), ft.Text("Reportes")]),
            padding=10,
            margin=ft.margin.only(bottom=5),
            ink=True,
            on_click=lambda _: page.go("/reports")
        ),
        ft.Container(
            content=ft.Row([ft.Icon(ft.icons.EXIT_TO_APP, color=ft.colors.ERROR), ft.Text("Salir", color=ft.colors.ERROR)]),
            padding=10,
            margin=ft.margin.only(top=20),
            ink=True,
            on_click=lambda _: cerrar_sesion(page)
        ),
    ]

    # Menu administrador
    if is_ad[0] == "Administrativo":
        admin_menu = ft.Column(
            [
                ft.Container(
                    content=ft.Row([ft.Icon(ft.icons.ADMIN_PANEL_SETTINGS), ft.Text("Administración")]),
                    padding=10,
                    margin=ft.margin.only(bottom=5),
                    ink=True,
                    on_click=lambda _: page.go("/admin")
                )
            ] + menu_items,
            spacing=10
        )
        return admin_menu
    else:
        user_menu = ft.Column(menu_items, spacing=10)
        return user_menu

def create_menu_container(page):
    return ft.Container(
        content=menu(page),
        width=250,
        bgcolor=ft.colors.SURFACE,
        padding=20,
        height=page.height,
    )