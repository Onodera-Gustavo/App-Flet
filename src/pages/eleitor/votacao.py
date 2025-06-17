import flet as ft
from flet import Page, View, Column, Row, Container, Divider, GridView
from flet import Text, ElevatedButton

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
    
    grid_cartoes = GridView(
        controls=[criar_cartoes("Data", f"Jogo {i}", i) for i in range(10)],
        runs_count=4,  # força 4 colunas
        max_extent=300,
        child_aspect_ratio=1,
        spacing=15,
        run_spacing=15,
        expand=True,
    )

    def votar():
        """Votar"""
        pass
        

    return View(
        route="/votacao",
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],
        
        controls=[
        Container(
            expand=True,
            content=Column(
                [
                    # HEADER
                    Container(
                        padding=10,
                        content=Row(
                            [
                                ft.Image(
                                    src="../assets/Logo.png",
                                    width=100,
                                    height=100,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                Column(
                                    [
                                        Text("Game Awards", style=AppConfig.get_text_style(page, "title_large")),
                                        Text("Game of the Decade", style=AppConfig.get_text_style(page, "title_small")),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ),
                    Container(expand=True, content=Divider(color=AppConfig.COLOR_PALETTE["accent"], height=1)),
                    
                    # CONTEÚDO COM SCROLL
                    Container(
                        padding=25,
                        content=Column(
                            [
                                Text("Selecione o jogo que deseja votar", style=AppConfig.get_text_style(page, "body_large")),
                                grid_cartoes,
                            ],
                            horizontal_alignment="center",
                            spacing=5,
                        )
                    ),
                    
                    
                    # FOOTER
                    Container(
                        padding=10,
                        content=Column(
                            [
                                Divider(color=AppConfig.COLOR_PALETTE["accent"], height=1),
                                Row(
                                    [
                                        Text("Termos de uso", style=AppConfig.get_text_style(page, "body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, "body_description")),
                                        Text("Política de privacidade", style=AppConfig.get_text_style(page, "body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, "body_description")),
                                        Text("Cookies", style=AppConfig.get_text_style(page, "body_description"))
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                                ),
                                Row(
                                    [
                                        Text("SENAI - SP", style=AppConfig.get_text_style(page, "body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, "body_description")),
                                        Text("Game Awards", style=AppConfig.get_text_style(page, "body_description")),
                                    ],
                                    alignment=ft.MainAxisAlignment.START
                                )
                            ],
                            spacing=5,
                        )
                    )
                ],
                expand=True
            )
        )
    ],
    scroll=ft.ScrollMode.AUTO
    )