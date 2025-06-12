import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField

from pages.function import aviso
from configuracao import AppConfig

def tela_menu(page: Page):

    button_style = AppConfig.get_elevated_button_style(page)

    cadastrar_button = ElevatedButton(
        text="Cadastrar",
        scale=1.3,
        width=200,
        on_click=lambda _: page.go("/cadastro"),
        style=button_style
    )

    remover_button = ElevatedButton(
        text="Remover",
        scale=1.3,
        width=200,
        # on_click=lambda _: ,
        style=button_style
    )

    editar_button = ElevatedButton(
        text="Editar",
        scale=1.3,
        width=200,
        # on_click=lambda _: ,
        style=button_style
    )

    relatorio_button = ElevatedButton(
        text="Relatório",
        scale=1.3,
        width=200,
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
                # bgcolor=AppConfig.COLOR_PALETTE["teste"],
                content=Column(
                    [
                        Container(
                            # bgcolor=AppConfig.COLOR_PALETTE["teste_2"],
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
                        Row(
                            [
                                Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["secondary"]),
                                Container(
                                    width=600,
                                    content=Column(
                                        [
                                            Row(
                                                    [
                                                        cadastrar_button,
                                                        remover_button,
                                                    ],
                                                    alignment= ft.MainAxisAlignment.SPACE_EVENLY
                                                ),
                                            Container(
                                                # bgcolor=AppConfig.COLOR_PALETTE["teste_3"],
                                                content=Column(
                                                    [
                                                        ft.Image(
                                                            src="../assets/Logo.png",
                                                            width=100,
                                                            height=100,
                                                            fit=ft.ImageFit.CONTAIN
                                                        )
                                                    ],
                                                    spacing=6
                                                ),
                                                
                                            ),
                                            Row(
                                                [
                                                    editar_button,
                                                    relatorio_button,
                                                ],
                                                alignment= ft.MainAxisAlignment.SPACE_EVENLY
                                            )
                                        ],
                                        alignment= ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment="center"
                                    )
                                ), 
                                Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["secondary"])
                            ],
                            height=400
                        ),
                        
                        Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["secondary"]),
                    ]
                )

            )#Container 
        ],#Control
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],  
    )

