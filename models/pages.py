# Importar las librerias necesarias
import flet as ft

# Importar las paginas
from pages.index import LoginPage
from pages.register import RegisterPage
from pages.Error404 import Error404
from pages.dashboard import Dashboard
from pages.damin import Dadmin
from pages.perfil import Profile
from pages.forgot import ForgotPage 
from pages.reportes import Reports
from pages.clientes import Clients

# Definir la funcion Pages que recibe un objeto de tipo Page
def Pages(page: ft.Page):
    if page.route == "/": # Definimos nuestra ruta inicial
        LoginPage(page)
    page.update()

# Modelo Vista Controlador en flet para cambiar ruta
    def route_change(route):
        page.clean()
        if page.route == "/register":
            page.clean()
            page.update()
            RegisterPage(page)
        elif page.route == "/":
            page.clean()
            page.update()
            LoginPage(page)
        elif page.route == "/dashboard":
            page.clean()
            page.update()
            Dashboard(page)
        elif page.route == "/admin":
            page.clean()
            page.update()
            Dadmin(page)
        elif page.route == "/me":
            page.clean()
            page.update()
            Profile(page)
        elif page.route == "/forgot":
            page.clean()
            page.update()
            ForgotPage(page)
        elif page.route == "/reports":
            page.clean()
            page.update()
            Reports(page)
        elif page.route == "/clients":
            page.clean()
            page.update()
            Clients(page)       
        else:
            page.clean()
            page.update()
            Error404(page)
        page.update()

    page.on_route_change = route_change
        

ft.app(target=Pages)