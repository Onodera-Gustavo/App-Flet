import flet as ft
from flet import Page, View, Text, ElevatedButton,  TextField
from flet import Column, Row

from pages.function import aviso, LettersOnlyInputFilter
from pages.function import text_field_style, elevated_button_style
from pages.db import carregar_candidatos, salvar_candidatos

def tela_cadastro(page: Page):
    """Cadastro de Candidatos"""
    candidatos = []
    # Campos do formulário (mantidos iguais)
    nome_field = TextField(label="Nome do candidato:", input_filter=LettersOnlyInputFilter(),  autofocus=True, **text_field_style)
    partido_field = TextField(label="Partido do candidato:", input_filter=LettersOnlyInputFilter(),  **text_field_style)
    numero_field = TextField(label="Número do candidato:", input_filter=ft.NumbersOnlyInputFilter(), max_length=2, **text_field_style)
    proposta_field = TextField(label="Proposta eleitoral:", max_length=100, multiline=True, min_lines=3, max_lines=5, **text_field_style)

    def cadastrar():
        """Cadastrar um novo candidato"""
        
        nome = nome_field.value
        partido = partido_field.value
        numero = numero_field.value
        proposta = proposta_field.value

        if not numero or not numero.isdigit() or len(numero) != 2 or not nome or not partido or not proposta:
            aviso(page, "Erro", "Preencha todos os campos corretamente.")
            return
        
        try:
            candidatos = carregar_candidatos(caminho="Candidato")
            
            # Verify the structure of loaded data
            if not all(isinstance(candidato, dict) for candidato in candidatos):
                aviso(page, "Erro", "Dados de candidatos corrompidos. Recriando arquivo.")
                candidatos = []
            
            if any(str(candidato.get("Numero Eleitoral", "")) == numero for candidato in candidatos):
                aviso(page, "Erro", "Número de candidato já cadastrado.")
                return
            
            candidato = {
                "Nome": nome,
                "Partido": partido,
                "Numero Eleitoral": int(numero),  # Store as integer
                "Votos": 0,
                "Proposta": proposta
            }
            
            candidatos.append(candidato)
            salvar_candidatos(candidatos, caminho="Candidato")
            
            aviso(page, "Sucesso", "Candidato cadastrado com sucesso!")
            
            # Limpa os campos
            nome_field.value = ""
            partido_field.value = ""
            numero_field.value = ""
            proposta_field.value = ""
            page.update()
            
        except Exception as ex:
            aviso(page, "Erro", f"Ocorreu um erro: {str(ex)}")


    return View(
        route="/cadastro",

        controls = [
            Column([
                    Text("Cadastro de Candidatos", size=48, weight="bold", color="#B5E0FD"), # type: ignore
                    Text("Preencha os campos abaixo para cadastrar um novo candidato.", size=16, color="#92B1C5")
                    ], 
                   spacing=-5,
                   horizontal_alignment="center" # type: ignore
                ),
            
            
            Column([
                Text("Nome:", size=16, color="#92B1C5"),
                nome_field,

                Text("Partido:", size=16, color="#92B1C5"),
                partido_field,

                Text("Número:", size=16, color="#92B1C5"),
                numero_field,

                Text("Proposta:", size=16, color="#92B1C5"),
                proposta_field
                ],
            spacing=10
            ),

            
            Column([
                ElevatedButton(text = "Cadastrar", scale = 1.3, width=200, on_click=lambda _: cadastrar(), style=elevated_button_style),
                ElevatedButton(text = "Retornar", scale = 1.3, width=200, on_click=lambda e: page.go("/"), style=elevated_button_style)
                ], 
                horizontal_alignment="center", # type: ignore
                spacing=20
                ),
            
        ],
        padding=40,
        spacing=60,
        horizontal_alignment="center", # type: ignore
        vertical_alignment="top" # type: ignore
    )