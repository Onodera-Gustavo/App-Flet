import flet as ft
from flet import Page, View, Column, Row, Container, Divider, GridView
from flet import Text, ElevatedButton, TextField

import requests

from pages.function import aviso, TelaBase
from configuracao import AppConfig



def tela_edicao(page: Page):
    """Cadastro de Candidatos"""
    tela = TelaBase(page)
    
    # Configurações de estilo
    text_field_style = AppConfig.get_text_field_style(page)
    button_style = AppConfig.get_elevated_button_style(page)

    base_url = "http://localhost:8000/jogos"  # URL base da API

    # Primeiro, vamos obter os dados da API
    jogos_disponiveis = []
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            jogos_disponiveis = response.json()["jogos_disponiveis"]
    except Exception as e:
        print(f"Erro ao obter jogos: {e}")

    def criar_cartoes(jogo: dict):
        """Cartões que recebem os jogos para votação"""
        return ft.Card(
            width=180,
            height=250,
            elevation=6,
            content=Container(
                border_radius=10,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    rotation=3,
                    end=ft.alignment.bottom_center,
                    colors=[AppConfig.COLOR_PALETTE["secondary"], AppConfig.COLOR_PALETTE["on_secondary"]]
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
                                        Text(value=str(jogo.get("releaseDate", "N/A")), 
                                             style=AppConfig.get_text_style(page, "label_bold")),
                                        Container(
                                            width=150,  # ajuste conforme seu layout
                                            content=Text(value=jogo.get("title", "Nome não disponível"), no_wrap=False, max_lines=2, overflow="ellipsis",
                                             style=AppConfig.get_text_style(page, "label_bold"))
                                        )
                                        
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ElevatedButton(
                                    text="Votar",
                                    scale=0.8,
                                    width=100,
                                    on_click=lambda _: abrir_edicao(jogo.get("id"), jogo.get("title")),
                                    style=button_style
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ],
                )  
            )
        )
    
    grid_cartoes = GridView(
        controls=[criar_cartoes(jogo) for jogo in jogos_disponiveis],
        runs_count=4,
        max_extent=300,
        child_aspect_ratio=1,
        spacing=15,
        run_spacing=15,
        expand=True,
    )

    corpo = Container(
        content= grid_cartoes
    )

    def abrir_edicao(id: int, nome: str ):
        nova_view = editar(id, nome)
        page.views.append(nova_view)
        page.go("/edicao/editar")

    
    def editar( id: int, nome: str):

        nome_field = TextField(
            label=f"Nome:", 
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
            on_click=lambda _: page.go("/edicao"),
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



        # Corpo principal
        corpo = Column(
            [
                Row(
                    [
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
            ]
        ) 

        
        return View(
            route="/edicao",
            controls= [tela.construir(body=corpo)]
            )
    
    return View(
        route="/edicao",
        controls= [tela.construir(body=corpo)],scroll=ft.ScrollMode.AUTO
    )
    