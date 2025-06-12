import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField

from pages.function import aviso
from configuracao import AppConfig

def tela_votacao(page: Page):
    """Votação de Alunos"""
    button_style = AppConfig.get_elevated_button_style(page)

    def cartoes(quantidade: int):
        """Cartões que recebem os jogos para votação"""
        contructo = []
        
        for i in range(quantidade):
            contructo.append(
                Container(
                    content=Row(
                        [
                            Container(
                                    content=Column(
                                        [
                                            ft.Image(
                                            src="../../assets/Logo.png",
                                            width=150,
                                            height=150,
                                            fit=ft.ImageFit.CONTAIN
                                            ),
                                            Row(
                                                    [
                                                        Column([
                                                            # data
                                                            # nome
                                                        ]),
                                                        # ElevatedButton
                                                    ]
                                                )
                                        ]
                                    )
                                )
                            
                        ]
                    )
                )
            )

    def votar():
        """Votar"""
        pass
        

    return View(
        route="/votacao",
        controls=[
            Container(
                expand = True,
                # bgcolor=AppConfig.COLOR_PALETTE["teste"],
                content=Column(
                    [
                        Container(
                            alignment=ft.alignment.top_left,
                            # bgcolor=AppConfig.COLOR_PALETTE["teste_2"],
                            content=Row(
                                [
                                    ft.Image(
                                        src="../../assets/Logo.png",
                                        width=150,
                                        height=150,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    Column(
                                        [
                                            Text(value="Game Awards", style=AppConfig.get_text_style(page, "title_large"),),
                                            Text(value="Game of the Decade", style=AppConfig.get_text_style(page, "title_small"),),
                                        ],
                                        
                                    )
                                ],
                            ),
                            
                        ),
                    ]
                )
                
            )#Container
        ],#Control
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],  
    )