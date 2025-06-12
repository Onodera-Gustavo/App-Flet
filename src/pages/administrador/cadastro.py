import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField

from pages.function import aviso, LettersOnlyInputFilter
from configuracao import AppConfig

def tela_cadastro(page: Page):
    """Cadastro de Candidatos"""
    
    text_field_style = AppConfig.get_text_field_style(page)
    button_style = AppConfig.get_elevated_button_style(page)

    
    nome_field = TextField(label="Nome do candidato:", input_filter=LettersOnlyInputFilter(),  autofocus=True, **text_field_style)
    genero_field = TextField(label="Partido do candidato:", input_filter=LettersOnlyInputFilter(),  **text_field_style)
    data_field = TextField(label="Número do candidato:", input_filter=ft.NumbersOnlyInputFilter(), **text_field_style)
    
    cadastrar_button = ElevatedButton(
        text="Cadastrar",
        scale=1.3,
        width=200,
        # on_click=lambda _:,
        style=button_style
    )
    
    Retornar_button = ElevatedButton(
        text="Cadastrar",
        scale=1.3,
        width=200,
        on_click=lambda _: page.go("/menu"),
        style=button_style
    )
    

    def cadastrar():
        """Cadastrar um novo candidato"""
        pass
       

    return View(
        route="/cadastro",
        controls = [
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
                                # Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["secondary"]),
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
                                        alignment="center",
                                        horizontal_alignment="center",
                                        spacing=6
                                    ),
                                    
                                ),
                                Column(
                                    [
                                        nome_field,
                                        genero_field,
                                        data_field,
                                        Column(
                                            [
                                                cadastrar_button,
                                                Retornar_button
                                            ],
                                            spacing=20,
                                            horizontal_alignment="center"
                                        )
                                        
                                    ],
                                    spacing=25,
                                    horizontal_alignment="center"
                                ),
                                # Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["secondary"]),
                            ],
                            height=400,
                            alignment= ft.MainAxisAlignment.SPACE_EVENLY
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
