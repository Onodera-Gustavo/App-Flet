import flet as ft
from flet import Page, View, Text, ElevatedButton
from flet import Column

from pages.function import elevated_button_style
def tela_menu(page: Page):

    def finalizar_secao():
        """Encerra a sessão do usuário"""
        # para retornar ao login
        #page.go("/")

        # para fechar a janela
        page.window.close()

    # Menu para o Administrador 
    return View(
        route="/menu",
        controls=[
            Text("Menu Principal", size=48, weight="bold", color="#B5E0FD"), # type: ignore
            Column(
                [
                ElevatedButton(text ="Cadastrar Candidato", scale = 1.3, width=180, on_click=lambda e: page.go("/cadastro"), style=elevated_button_style),
                ElevatedButton(text ="Relatório", scale = 1.3, width=180, on_click=lambda _: page.go("/relatorio"), style=elevated_button_style),
                ElevatedButton(text ="Reiniciar Votação", scale = 1.3, width=180, style=elevated_button_style),
                ElevatedButton(text ="Encerrar Votação", scale = 1.3, width=180, style=elevated_button_style),
                ElevatedButton(text ="Finalizar", scale = 1.3, width=180, on_click= lambda _: finalizar_secao(), style=elevated_button_style),
                ], 
                horizontal_alignment="center", # type: ignore
                spacing=30,
            )
        ],
        
        spacing=40,
        horizontal_alignment="center", # type: ignore
        vertical_alignment="center" # type: ignore
    )
