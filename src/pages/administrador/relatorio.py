import flet as ft
from flet import Page, View, Text, ElevatedButton
from flet import Column, Row

from pages.function import aviso, elevated_button_style
from pages.db import carregar_candidatos, escolher_caminho


def tela_relatorio(page: Page):
    """Imprimir Relatório de Votação"""

    candidatos = carregar_candidatos(caminho="Candidato")
    total_votos = sum(candidato["Votos"] for candidato in candidatos)
    
    resultado = ft.Column()
    
    if total_votos > 0:
        for candidato in sorted(candidatos, key =lambda c: c["Votos"], reverse = True):
            resultado.controls.append(ft.Column( controls=[
                Text(value = "Candidato: " + candidato["Nome"]),
                Text(value = "Partido: " + candidato["Partido"]),
                Text(value = "Votos: " + str(candidato["Votos"])),
                ft.Divider()
                ],
                horizontal_alignment="center", # type: ignore
                spacing=20
            ))

    else:
        resultado.controls.append(Text(value = "Não a votos validos"))

    def importar():
        """Importar Relatório de Votação"""
        
        linhas_relatorio = []
        linhas_relatorio.append(f"RELATÓRIO DE VOTAÇÃO\nTotal de votos: {total_votos}\n\n")

        if total_votos > 0:
            for candidato in sorted(candidatos, key = lambda c: c["Votos"], reverse = True):
                texto = f"{candidato['Nome']} ({candidato['Partido']}): {candidato['Votos']} Votos"
                linhas_relatorio.append(texto)
        try:
            with open(escolher_caminho(caminho="Proposta"), "w", encoding="utf-8") as arquivo:
                arquivo.write(f"RELATÓRIO DE VOTAÇÃO\nTotal de votos: {total_votos}\n\n")
                arquivo.write("\n".join(linhas_relatorio))
            aviso(page, "Sucesso", "Relatório exportado com sucesso!")

        except Exception as e:
            aviso(page, "Erro", f"Falha ao exportar relatório: {str(e)}")

    return View(
        route="/relatorio",

        controls = [
            Column([
                    Text(value = "Relatório de Votação", size=24, weight="bold", color="#B5E0FD")
                ],
                spacing=20,
                horizontal_alignment="center", # type: ignore
            ),

            resultado,

            Row([
                ElevatedButton(text="Exportar", width=180, scale = 1.3, on_click=lambda _:importar(), style=elevated_button_style),
                ElevatedButton(text="Retornar", width=180, scale = 1.3, on_click=lambda _: page.go("/"), style=elevated_button_style),
            ], 
            spacing=60,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment="end" # type: ignore
            )
        ],
        padding=40,
        spacing=60,
        horizontal_alignment="center", # type: ignore
    )