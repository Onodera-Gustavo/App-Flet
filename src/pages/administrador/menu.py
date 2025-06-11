import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField

from pages.function import aviso
from configuracao import AppConfig

def tela_menu(page: Page):

    button_style = AppConfig.get_elevated_button_style(page)

    cadastrar_button = ElevatedButton(
        text="Entrar",
        scale=1.3,
        width=250,
        # on_click=lambda _: ,
        style=button_style
    )

    remover_button = ElevatedButton(
        text="Entrar",
        scale=1.3,
        width=250,
        # on_click=lambda _: ,
        style=button_style
    )

    editar_button = ElevatedButton(
        text="Entrar",
        scale=1.3,
        width=250,
        # on_click=lambda _: ,
        style=button_style
    )

    relatorio_button = ElevatedButton(
        text="Entrar",
        scale=1.3,
        width=250,
        # on_click=lambda _: ,
        style=button_style
    )

    def finalizar_secao():
        """Encerra a sessão do usuário"""
        #para retornar ao login
        page.go("/")

    # Menu para o Administrador 
    return View(
        route="/menu",
        controls=[
            Container(
                expand = True,
                bgcolor=AppConfig.COLOR_PALETTE["error"],
                content=Column(
                    [
                         Container(
                            # bgcolor=AppConfig.COLOR_PALETTE["secondary"],
                            content=Column(
                                [
                                    ft.Image(
                                        src="../assets/Logo.png",
                                        width=150,
                                        height=150,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    Divider(color=AppConfig.COLOR_PALETTE["accent"], height=1),
                                ],
                                horizontal_alignment="center",
                                spacing=6
                            ),
                            
                        ),
                        Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["secondary"]),
                        Container(
                            content=Column(
                                [

                                ]
                            )
                        )
                    ]
                )

            )#Container 
        ],#Control
        horizontal_alignment="center",
        vertical_alignment="center",
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],  
    )

