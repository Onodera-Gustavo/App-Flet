import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField, TextButton

from pages.function import aviso
from configuracao import AppConfig

def tela_login(page: Page):
    
    
    text_field_style = AppConfig.get_text_field_style(page)

    identificacao_field = TextField(
        label="Identificação",
        autofocus=True,
        width=400,
        prefix_icon=ft.Icons.PERSON,
        **text_field_style
    )

    senha_field = TextField(
        label="Senha",
        width=400,
        prefix_icon=ft.Icons.LOCK,
        **text_field_style,
        password=True,
        can_reveal_password=True
    )

    login_button = ElevatedButton(
        text="Entrar",
        scale=1.3,
        width=250,
        on_click=lambda _: filtro_usuarios(),
        style= AppConfig.get_elevated_button_style(page)
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
                expand = True,
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
                                    Divider(color=AppConfig.COLOR_PALETTE["accent"], height=1),
                                ],
                                horizontal_alignment="center",
                                spacing=6
                            ),
                            
                        ),
                        Container(expand=True),
                        Text("Login", style=AppConfig.get_text_style(page, style_type="title_medium")),
                        Column(
                            [
                                identificacao_field,
                                senha_field,
                                Column(
                                    [
                                        login_button,
                                        Row(
                                            [
                                                TextButton("Esqueci a senha", on_click=lambda _: page.go("/cad_esqu"), style=AppConfig.get_elevated_button_style(page, "background", "text", "body_description", False)),
                                                Text("|", style=AppConfig.get_text_style(page, style_type="body_description")),
                                                TextButton("Cadastrar", on_click=lambda _: page.go("/cad_esqu"), style=AppConfig.get_elevated_button_style(page, "background", "text", "body_description", False))
                                            ],
                                            spacing=20,
                                            alignment=ft.MainAxisAlignment.CENTER
                                        )
                                    ],
                                    horizontal_alignment="center",
                                    spacing=10,
                                    
                                )
                            ],
                            horizontal_alignment="center",
                            spacing=30,
                        ),
                        Container(expand=True),
                        Column(
                            [
                                Row(
                                    [
                                        Text("Termos de uso", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("Política de privacidade", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("Cookies", style=AppConfig.get_text_style(page, style_type="body_description"))
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                                ),
                                Divider(color=AppConfig.COLOR_PALETTE["accent"], height=1),
                                Row(
                                    [
                                        Text("SENAI - SP", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("|", style=AppConfig.get_text_style(page, style_type="body_description")),
                                        Text("Game Awards", style=AppConfig.get_text_style(page, style_type="body_description"))
                                    ],
                                    alignment=ft.MainAxisAlignment.START
                                )
                            ],
                            
                            spacing=4,
                        )


                        
                    ],
                    spacing= 10,
                    horizontal_alignment="center",

                )  
            )#Container 
        ],#Control
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],  
    )
