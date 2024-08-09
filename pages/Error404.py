import flet as ft
from models.pages import *
from config.settings import titulo, tema

def Error404(page: ft.Page):
    page.clean()
    page.update()
    page.title = titulo
    page.theme_mode = tema
    page.add(ft.SafeArea(ft.Text("Page not found")))
    page.update()