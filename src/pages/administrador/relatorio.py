import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField, TextButton, Image


from pages.function import aviso
from configuracao import AppConfig
from pages.db import carregar_candidatos, escolher_caminho

import matplotlib.pyplot as plt

def tela_relatorio(page: Page):
    """Imprimir Relatório de Votação"""
    style = AppConfig.get_elevated_button_style(page)
    exportar = ElevatedButton(text="Exportar", width=180, scale=1.3, on_click=lambda _: importar(), style=style),
    retorno = ElevatedButton(text="Retornar", width=180, scale=1.3, on_click=lambda _: page.go("/menu"), style=style),
    
    candidatos = carregar_candidatos(caminho="Candidato")
    total_votos = sum(candidato["Votos"] for candidato in candidatos)
    
    # resultado = ft.Column()

    nomes = []
    votos = []

    if total_votos > 0:
        for candidato in sorted(candidatos, key=lambda c: c["Votos"], reverse=True):
            # resultado.controls.append(
            #     ft.Column(
            #         controls=[
            #             Text(value="Candidato: " + candidato["Nome"]),
            #             Text(value="Partido: " + candidato["Partido"]),
            #             Text(value="Votos: " + str(candidato["Votos"])),
            #             ft.Divider()
            #         ],
            #         spacing=10
            #     )
            # )
            nomes.append(candidato["Nome"])
            votos.append(candidato["Votos"])
    else:
        # resultado.controls.append(Text(value="Não há votos válidos"))
        pass

    def gerar_grafico():
        """Gerar gráfico e salvar como imagem"""
        cores = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF']  # Altere as cores aqui!
        plt.figure(figsize=(6,4))
        plt.bar(nomes, votos, color=cores[:len(nomes)])
        plt.title('Resultado da Votação')
        plt.xlabel('Candidatos')
        plt.ylabel('Votos')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("grafico_votacao.png")
        plt.close()

    gerar_grafico()

    def importar():
        """Exportar relatório de votação"""
        linhas_relatorio = [f"RELATÓRIO DE VOTAÇÃO\nTotal de votos: {total_votos}\n\n"]
        if total_votos > 0:
            for candidato in sorted(candidatos, key=lambda c: c["Votos"], reverse=True):
                texto = f"{candidato['Nome']} ({candidato['Partido']}): {candidato['Votos']} Votos"
                linhas_relatorio.append(texto)
        try:
            with open(escolher_caminho(caminho="Proposta"), "w", encoding="utf-8") as arquivo:
                arquivo.write("\n".join(linhas_relatorio))
            aviso(page, "Sucesso", "Relatório exportado com sucesso!")
        except Exception as e:
            aviso(page, "Erro", f"Falha ao exportar relatório: {str(e)}")



    return View(
        route="/relatorio",
        controls=[
            Column([
                Text("Relatório de Votação", size=54, weight="bold", color="#B5E0FD")
            ], 
            spacing=20, 
            horizontal_alignment="center"
            ),
            # resultado,
            Image(src="grafico_votacao.png", width=600, height=400),
            Row([
                exportar,
                retorno
            ], 
            spacing=60, 
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            width=540
            )
        ],
        spacing=60,
        horizontal_alignment="center", 
        vertical_alignment="center" 
    )
