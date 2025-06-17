import flet as ft
from flet import *

import requests
import sqlite3

def obter_dados():
    """Obtém dados dos jogos via API"""
    try:
        resposta = requests.get("http://localhost:8000/jogos")
        if resposta.status_code == 200:
            dados = resposta.json()["jogos_disponiveis"]
            return dados
        else:
            return []
    except Exception as e:
        print("Erro ao acessar API:", e)
        return []

def tela_relatorio(page: ft.Page):
    """View com tabela baseada nos dados do banco de dados"""

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Partido")),
            ft.DataColumn(ft.Text("Votos")),
        ],
        rows=[]
    )

    # Adiciona os dados na tabela
    for jogo in obter_dados():
        tabela.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(jogo.get("id", "N/A")))),
                    ft.DataCell(ft.Text(jogo.get("title", "N/A"))),
                    ft.DataCell(ft.Text(jogo.get("genre", "N/A"))),
                    ft.DataCell(ft.Text(str(jogo.get("releaseDate", "N/A")))),
                ]
            )
        )

    return ft.View(
        route="/relatorio",
        controls=[
            ft.Column([
                ft.Text("Resultados da Votação", size=32, weight=ft.FontWeight.BOLD),
                tabela,
                ft.Row([
                    ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/menu"))
                ])
            ],
            spacing=30,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ],
        scroll=ScrollMode.AUTO,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )