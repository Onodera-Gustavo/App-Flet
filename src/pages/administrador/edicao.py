import flet as ft
from flet import Page, View, Column, Row, Container, Divider, GridView
from flet import Text, ElevatedButton

from pages.function import aviso, TelaBase
from configuracao import AppConfig



def tela_edicao(page: Page):
    """Cadastro de Candidatos"""
    tela = TelaBase(page)
    
    # Configurações de estilo
    text_field_style = AppConfig.get_text_field_style(page)
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
                    rotation= 5,
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
                                    text="Editar",
                                    scale=0.8,
                                    width=100,
                                    on_click=lambda _: editar(i),
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
        controls=[criar_cartoes("Data", f"Jogo {i}", i) for i in range(15)],
        runs_count=4,  # força 4 colunas
        max_extent=300,
        child_aspect_ratio=1,
        spacing=15,
        run_spacing=15,
        expand=True,
    )
    
    corpo = Container(
        content= grid_cartoes
    )
    
    def editar(data: str, nome: str, i: int):
        corpo = Container(
            content= Column(
            
        ))
        return View(
            route="/edicao",
            controls= [tela.construir(body=corpo)]
            )
    
    return View(
        route="/edicao",
        controls= [tela.construir(body=corpo)],scroll=ft.ScrollMode.AUTO
    )
    