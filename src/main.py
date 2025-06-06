import flet as ft
from flet import RouteChangeEvent, Page

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from pages.login import tela_login

from pages.administrador.menu import tela_menu
from pages.administrador.cadastro import tela_cadastro
from pages.administrador.relatorio import tela_relatorio

from pages.eleitor.votacao import tela_votacao

from configuracao import configurar_app



def main(page: Page) -> None:

    configurar_app(page)
        
    # Configurações de tema e tamanho
    page.theme_mode = "dark"

    page.window.width = 1024  # Largura inicial
    page.window.height = 768  # Altura inicial
    page.window.min_width = 800  # Largura mínima
    page.window.min_height = 600  # Altura mínima
    
    def route_change(e: RouteChangeEvent) -> None:
        """Evento de mudança de rota"""
        page.views.clear()

        if page.route == "/":
            page.views.append(tela_login(page))

        if page.route == "/menu":
            page.views.append(tela_menu(page))

        elif page.route == "/cadastro":
            page.views.append(tela_cadastro(page))

        elif page.route == "/votacao":
            page.views.append(tela_votacao(page))

        elif page.route == "/relatorio":
            page.views.append(tela_relatorio(page))

        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)
    

if __name__ == '__main__':
    # Para desktop e web
    ft.app(target=main)
    
    # Para mobile (usando Flet app)
    #ft.app(target=main, view=ft.AppView.FLET_APP)