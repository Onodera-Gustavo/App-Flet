import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField

from pages.function import aviso
from configuracao import AppConfig

def tela_votacao(page: Page):
    """Votação de Alunos"""
    button_style = AppConfig.get_elevated_button_style(page)

    def criar_cartoes(data: str, nome: str, i: int):

        """Cartões que recebem os jogos para votação"""
        cartao = ft.Card(
            width=180,
            height=250,
            elevation=6,
            content=Container(
                border_radius=10,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    rotation= 3,
                    end=ft.alignment.bottom_center,
                    colors=[AppConfig.COLOR_PALETTE["secondary"],AppConfig.COLOR_PALETTE["on_secondary"]]
                ),
                padding=5,
                content=Column(
                    [   
                        Container(
                            alignment=ft.alignment.top_center,
                            
                            content=Column(
                                [
                                    ft.Image(
                                        src="../assets/Logo.png",
                                        width=150,
                                        height=150,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                ],
                                horizontal_alignment="center",
                            ),
                        ),
                        
                        Row(
                            [
                                Column(
                                    [
                                        Text(value=data, style=AppConfig.get_text_style(page, "body_description"),),
                                        Text(value=nome, style=AppConfig.get_text_style(page, "body_description"),),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                    
                                ),
                                # elevated button
                                ElevatedButton(
                                    text="Votar",
                                    scale=0.8,
                                    width=100,
                                    on_click=lambda _: votar(),
                                    style=button_style
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                     ],#Control
                                    
                )  
            )#Container 
        )#Card 

        return cartao
    
    cartoes=[ criar_cartoes(data="data", nome="nome", i=0) for i in range(3) ]

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
                                        src="../assets/Logo.png",
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
                        Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["success"]),
                        
                        Row(
                            width=300,
                            controls=cartoes
                        ),

                        Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["success"]),
                        Column(
                            [
                                Row(
                                    [
                                        Text("Termos de uso", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("Política de privacidade", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("Cookies", style=AppConfig.get_text_style(page, style_type="body_description"))
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                                ),
                                Divider(color=AppConfig.COLOR_PALETTE["accent"], height=1),
                                Row(
                                    [
                                        Text("SENAI - SP", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("Game Awards", style=AppConfig.get_text_style(page, style_type="body_description"))
                                    ],
                                    alignment=ft.MainAxisAlignment.START
                                )
                            ],
                            
                            spacing=4,
                        )
                    ],
                    scroll= ft.ScrollMode.ALWAYS
                )
                
            )#Container
        ],#Control
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],  
    )