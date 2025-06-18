import flet as ft
from flet import *

import requests
import sqlite3
import json

from pages.function import aviso, TelaBase
from configuracao import AppConfig

def obter_dados():
    """Obtém dados dos jogos via API"""
    try:
        resposta = requests.get("http://localhost:8000/jogos")
        if resposta.status_code == 200:
            dados = resposta.json()["jogos_disponiveis"]
            print("Dados recebidos:", dados)  # <-- Adicione isto
            return dados
        else:
            return []
    except Exception as e:
        print("Erro ao acessar API:", e)
        return []

def tela_relatorio(page: ft.Page):
    """View com tabela baseada nos dados do banco de dados"""
    tela = TelaBase(page)

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Titulo")),
            ft.DataColumn(ft.Text("Genero")),
            ft.DataColumn(ft.Text("Data de Lancamento")),
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
        
    body = Column(
        [
            Text("Resultados da Votação", size=32, weight=ft.FontWeight.BOLD),
            tabela,
            Row(
                [
                    ElevatedButton("Voltar", on_click=lambda _: page.go("/menu"), style = AppConfig.get_elevated_button_style(page, text_style = "body_small")),
                ]
            )
        ],
        spacing=30,
        horizontal_alignment=CrossAxisAlignment.CENTER
    )

    return View(
        route="/relatorio",
        controls=[tela.construir(body)],
        scroll=ScrollMode.AUTO,
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER
    )