import flet as ft
from flet import Page, View, Text, ElevatedButton, TextField, Container
from flet import Column

from pages.function import aviso
from configuracao import AppConfig

def tela_login(page: Page):
    print("Criando tela de login") 
    
    text_field_style = AppConfig.get_text_field_style(page)
    button_style = AppConfig.get_elevated_button_style(page)

    identificacao_field = TextField(
        label="Identificação",
        autofocus=True,
        prefix_icon=ft.Icons.PERSON,
        **text_field_style
    )

    senha_field = TextField(
        label="Senha",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        **text_field_style
    )

    login_button = ElevatedButton(
        text="Entrar",
        scale=1.3,
        on_click=lambda _: filtro_usuarios(),
        style=button_style
    )

    def filtro_usuarios():
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
                width=page.width,
                height=page.height,
                bgcolor=AppConfig.COLOR_PALETTE["background"],
                content=Column(
                    [
                        Text("Login", size=48, weight="bold", color="#B5E0FD"),
                        identificacao_field,
                        senha_field,
                        login_button
                    ],
                    horizontal_alignment="center",
                    alignment="center",
                    spacing=30,
                ),
                alignment=ft.alignment.center,
            )
        ],
        padding=0,
        spacing=0
    )
