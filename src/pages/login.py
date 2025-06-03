import flet as ft
from flet import Page, View, Text, ElevatedButton, TextField, Container
from flet import Column, Row

from pages.function import aviso, text_field_style, elevated_button_style

def tela_login(page: Page):
    identificacao_field = TextField(label="Identificação", autofocus=True, prefix_icon=ft.Icons.PERSON, **text_field_style)
    senha_field = TextField(label="Senha", password=True, can_reveal_password=True, prefix_icon=ft.Icons.LOCK, **text_field_style)

    def filtro_usuarios(e):
        inde = identificacao_field.value.strip()
        senha = senha_field.value.strip()

        if inde == 'admin' and senha == 'admin':
            page.go("/menu")

        elif inde == 'eleitor' and senha == 'eleitor':
            page.go("/votacao")
            
        else:
            aviso(page, "Erro", "Usuário ou senha incorretos.")

    return View(
        route="/",
        controls=[
            Container(
                alignment=ft.alignment.center,
                padding=20,
                width=500,
                content=Column(
                    [
                        Text("Login", size=48, weight="bold", color="#B5E0FD"),
                        identificacao_field,
                        senha_field,
                        ElevatedButton(
                            text="Entrar",
                            scale=1.3,
                            width=180,
                            on_click=filtro_usuarios,
                            style=elevated_button_style
                        ),
                    ],
                    horizontal_alignment="center",
                    spacing=30,
                )
            )
        ],
        horizontal_alignment="center",
        vertical_alignment="center",
    )
