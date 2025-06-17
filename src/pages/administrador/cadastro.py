import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField, TextStyle, FontWeight

from pages.function import aviso
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
        autofocus=True, 
        **text_field_style
    )
    
    genero_field = TextField(
        label="Gênero:", 
        width=356, 
        height=45, 
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
    cadastrar_button = ElevatedButton(
        text="Cadastrar",
        width=356,
        height=34,
        style=AppConfig.get_elevated_button_style(page, text_style = "body_small")
    )

    retornar_button = ElevatedButton(
        text="Retornar",
        width=356,
        height=34,
        on_click=lambda _: page.go("/menu"),
        style=AppConfig.get_elevated_button_style(page, bg_color = "surface", text_style="body_small", on_hover="on_tertiary")
    )
    
    # Estado da imagem carregada
    imagem_preview = ft.Image(
        src="../assets/add_image.png",
        width=295,
        height=415,
        fit=ft.ImageFit.CONTAIN
    )

    file_picker = ft.FilePicker()

    def selecionar_imagem(e):
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["jpg", "jpeg", "png"])

    def imagem_selecionada(e: ft.FilePickerResultEvent):
        if e.files:
            imagem_preview.src = e.files[0].path
            page.update()

    file_picker.on_result = imagem_selecionada
    page.overlay.append(file_picker)


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
                        # Coluna da imagem com clique para escolher
                Container(
                    content=Column(
                        [
                            Container(
                                content=imagem_preview,
                                on_click=selecionar_imagem,
                                ink=True,  # feedback visual do clique
                                border_radius=8,
                                padding=10
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
                                spacing=30,
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