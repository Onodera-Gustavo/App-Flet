import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField, TextStyle, FontWeight

from pages.function import aviso, LettersOnlyInputFilter
from configuracao import AppConfig



def tela_cadastro(page: Page):
    """Cadastro de Candidatos"""
    
    # Configurações de estilo
    text_field_style = AppConfig.get_text_field_style(page)
    
    # Campos de texto
    nome_field = TextField(
        label="Nome:", 
        width=356, 
        height=45, 
        input_filter=LettersOnlyInputFilter(), 
        autofocus=True, 
        **text_field_style
    )
    
    genero_field = TextField(
        label="Gênero:", 
        width=356, 
        height=45, 
        input_filter=LettersOnlyInputFilter(), 
        **text_field_style
    )
    
    data_field = TextField(
        label="Ano de lançamento", 
        width=356, 
        height=45, 
        input_filter=ft.NumbersOnlyInputFilter(), 
        **text_field_style
    )
    
    # Botões
    # Na definição dos botões, substitua:
    cadastrar_button = ElevatedButton(
        text="Cadastrar",
        width=356,
        height=34,
        style=AppConfig.get_elevated_button_style(page, "primary", "body_small")  # Use cadastrar_style em vez de button_style
    )

    retornar_button = ElevatedButton(
        text="Retornar",
        width=356,
        height=34,
        on_click=lambda _: page.go("/menu"),
        style=AppConfig.get_elevated_button_style(page, "secundary")  # Use retornar_style em vez de button_style
    )

    # Layout principal
    
    # Layout principal
    content_column = Column(
        [
            # Cabeçalho com logo
            Container(
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
                )
            ),
            
            # Espaço flexível
            Container(expand=True),
            
            # Corpo principal
            Row(
                [
                    # Coluna da imagem
                    Container(
                        content=Column(
                            [
                                ft.Image(
                                    src="../assets/add_image.png",
                                    width=295,
                                    height=415,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                Divider(color=AppConfig.COLOR_PALETTE["accent"], height=1),
                            ],
                            alignment="center",
                            horizontal_alignment="center",
                            spacing=6
                        ),
                        padding=ft.padding.only(right=65)
                    ),
                    
                    # Coluna dos campos de formulário
                    Column(
                        [
                            nome_field,
                            genero_field,
                            data_field,
                            Column(
                                [
                                    cadastrar_button,
                                    retornar_button
                                ],
                                spacing=25,
                                horizontal_alignment="center"
                            )
                        ],
                        spacing=60,
                        horizontal_alignment="center"
                    ),
                ],
                height=400,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            
            # Espaço flexível
            Container(expand=True),
            
            # Rodapé
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
        ]
    )  # Remova a vírgula aqui

    return View(
        route="/cadastro",
        controls=[Container(expand=True, content=content_column)],
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],
    )