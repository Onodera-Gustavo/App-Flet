import flet as ft
from flet import View, Page, Text, ElevatedButton, TextField, Column, Row
from pages.function import aviso, elevated_button_style, text_field_style
from pages.db import carregar_candidatos, salvar_candidatos, atualizar
import json

def tela_votacao(page: Page):
    """Votação de Alunos"""

    # Campos do formulário
    alun_nome = TextField(label="Nome do aluno:", autofocus=True, **text_field_style)
    alun_matricula = TextField(
        label="Matrícula do aluno:", 
        input_filter=ft.NumbersOnlyInputFilter(), 
        max_length=4,
        **text_field_style
    )
    alun_voto = TextField(
        label="Número do candidato:", 
        input_filter=ft.NumbersOnlyInputFilter(), 
        max_length=2,
        **text_field_style
    )

    def votar():
        """Votar por aluno"""

        nome = alun_nome.value.strip()
        matricula = alun_matricula.value.strip()
        voto = alun_voto.value.strip()

        # Validação básica dos campos
        if not nome or not voto or not matricula or not matricula.isdigit() or not voto.isdigit():
            aviso(page, "Erro", "Preencha todos os campos corretamente.")
            return
        
        try:
            # Carrega os dados atuais
            alunos = carregar_candidatos(caminho="Aluno")
            candidatos = carregar_candidatos(caminho="Candidato")

            # Verifica se o aluno já votou
            aluno_existente = None
            for aluno in alunos:
                if aluno.get("matricula") == matricula:
                    if aluno.get("votou", False):
                        aviso(page, "Erro", "Esta matrícula já votou.")
                        return
                    aluno_existente = aluno
                    break

            # Verifica se o candidato existe
            candidato_encontrado = None
            for candidato in candidatos:
                if str(candidato.get("Numero Eleitoral", "")) == voto:
                    candidato_encontrado = candidato
                    break
            
            if not candidato_encontrado:
                aviso(page, "Erro", "Número de candidato inválido.")
                return

            # Atualiza os dados
            if aluno_existente:
                # Atualiza aluno existente
                aluno_existente["votou"] = True
                aluno_existente["nome"] = nome  # Atualiza nome caso tenha mudado
            else:
                # Adiciona novo aluno
                alunos.append({
                    "nome": nome,
                    "matricula": matricula,
                    "votou": True
                })
            
            # Incrementa voto do candidato
            candidato_encontrado["Votos"] = candidato_encontrado.get("Votos", 0) + 1

            # Salva as alterações
            salvar_candidatos(alunos, caminho="Aluno")
            salvar_candidatos(candidatos, caminho="Candidato")

            # Atualiza via função atualizar (para garantir consistência)
            atualizar(nome, matricula, caminho="Aluno")

            aviso(page, "Sucesso", "Voto registrado com sucesso!")

            # Limpa os campos
            alun_nome.value = ""
            alun_matricula.value = ""
            alun_voto.value = ""
            page.update()

        except Exception as ex:
            aviso(page, "Erro", f"Ocorreu um erro: {str(ex)}")

    return View(
        route="/votacao",
        controls=[
            Column([
                Text("Votação", size=48, weight="bold", color="#B5E0FD"),
                Text("Preencha os campos abaixo para Votar", size=16, color="#92B1C5"),
            ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            
            Column([
                Text("Nome:", size=16, color="#92B1C5"),
                alun_nome,
                Text("Matrícula:", size=16, color="#92B1C5"),
                alun_matricula,
                Text("Número do Candidato:", size=16, color="#92B1C5"),
                alun_voto
            ], spacing=10),
            
            Row([
                ElevatedButton(
                    text="Votar", 
                    scale=1.3, 
                    width=200, 
                    on_click=lambda _: votar(), 
                    style=elevated_button_style
                ),
                ElevatedButton(
                    text="Retornar", 
                    scale=1.3, 
                    width=200, 
                    on_click=lambda _: page.go("/"), 
                    style=elevated_button_style
                )
            ], spacing=80, alignment=ft.MainAxisAlignment.CENTER)
        ],
        padding=40,
        spacing=30,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )