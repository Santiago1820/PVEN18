import flet as ft
from models.pages import *

def main(page: ft.Page):
    Pages(page)
    page.on_route_change = Pages(page)

ft.app(target=Pages, assets_dir="assets")