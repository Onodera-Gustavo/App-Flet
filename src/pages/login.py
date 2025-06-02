import flet as ft
from flet import Page, View, Text, ElevatedButton, TextField
from flet import Column, Row

from pages.function import aviso, text_field_style, elevated_button_style

def tela_login (page: Page):

    identificacao_field = TextField(label="Identificação:", autofocus=True, **text_field_style)
    senha_field = TextField(label="Senha:", password=True, **text_field_style)

    def filtro_usuarios():
        """Validação de usuários"""
        inde = identificacao_field.value
        senha = senha_field.value

        if inde == 'admin' and senha == 'admin':
            page.go("/menu"),
        else:
            aviso(page, "Erro", "Usuário ou senha incorretos.")


    return View(
        route="/",
        controls=[
            Text("Login", size=48, weight="bold", color="#B5E0FD"), # type: ignore
            Column(
                    [
                    identificacao_field,
                    senha_field,
                    ElevatedButton(text ="Entrar", scale = 1.3, width=180, on_click=lambda _: filtro_usuarios() , style=elevated_button_style), # type: ignore
                    ], 
                    horizontal_alignment="center", # type: ignore
                    spacing=30,
                )
            ]
        )