import flet as ft
from flet import RouteChangeEvent, Page

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from pages.login import tela_login

from pages.administrador.menu import tela_menu
from pages.administrador.cadastro import tela_cadastro
from pages.administrador.relatorio import tela_relatorio
from pages.administrador.edicao import tela_edicao

from pages.secundario.cad_esqu import tela_cad_esqu

from pages.eleitor.votacao import tela_votacao

from configuracao import configurar_app

def main(page: Page) -> None:

    configurar_app(page)
    
    def route_change(e: RouteChangeEvent) -> None:
        """Evento de mudança de rota"""
        page.views.clear()

        # Use para ir direto a página que deseja
        # if page.route == "/":
        #     page.views.append(tela_cad_esqu(page))

        if page.route == "/":
            page.views.append(tela_login(page))
            
        elif page.route == "/votacao":
            page.views.append(tela_votacao(page))

        elif page.route == "/menu":
            page.views.append(tela_menu(page))

        elif page.route == "/cadastro":
            page.views.append(tela_cadastro(page))

        elif page.route == "/relatorio":
            page.views.append(tela_relatorio(page))
            
        elif page.route == "/edicao":
            page.views.append(tela_edicao(page))
        
        elif page.route == "/edicao/editar":
            page.views.append(tela_edicao.editar(page))
            
        elif page.route == "/cad_esqu":
            page.views.append(tela_cad_esqu(page))
            
            

        page.update()
    
    page.on_route_change = route_change

    if not page.route or page.route == "":
        page.go("/")
    else:
        page.go(page.route)
    
    

if __name__ == '__main__':
    # Para desktop e web
    ft.app(target=main)
    
    # Para mobile (usando Flet app)
    #ft.app(target=main, view=ft.AppView.FLET_APP)