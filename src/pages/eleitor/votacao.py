import flet as ft
from flet import Page, View, Column, Row, Container, Divider, GridView
from flet import Text, ElevatedButton, TextField

import requests

from pages.function import aviso
from configuracao import AppConfig

def tela_votacao(page: Page):
    """Votação de Alunos"""
    
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
                                    on_click=lambda _: votar(jogo.get("id"), jogo.get("title")),
                                    style=button_style
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ],
                )  
            )
        )

    def votar(id_jogo: int, nome_jogo: str):
        """Envia o voto para o backend"""
        try:
            # Dados para enviar ao backend - convertendo votado para bytes
            dados_voto = {
                "votado": True,  
                "nome_jogo": nome_jogo,
                "usuario": "usuario_teste"  # Adicione um usuário padrão ou obtenha do sistema
            }
            
            # Envia a requisição POST para a API
            response = requests.post(
                "http://localhost:8000/votar",
                json=dados_voto
            )
            
            if response.status_code == 200:
                aviso(page, "Voto Confirmado", "Seu voto foi registrado com sucesso!")
            else:
                aviso(page, "error", f"Erro ao votar: {response.json().get('detail', 'Erro desconhecido')}")
                
        except Exception as e:
            aviso(page, "error", f"Erro de conexão: {str(e)}")

    # Cria os cartões com os dados reais da API
    grid_cartoes = GridView(
        controls=[criar_cartoes(jogo) for jogo in jogos_disponiveis],
        runs_count=4,
        max_extent=300,
        child_aspect_ratio=1,
        spacing=15,
        run_spacing=15,
        expand=True,
    )
        

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