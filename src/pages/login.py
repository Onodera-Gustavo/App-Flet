import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField

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
        prefix_icon=ft.Icons.LOCK,
        **AppConfig.get_text_field_style(page, is_password = True)
    )

    login_button = ElevatedButton(
        text="Entrar",
        scale=1.5,
        width=250,
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
                
                content=Column(
                    [   
                        Container(
                            image=ft.Image(
                                src=f"../assets/Logo.png",
                                width=100,
                                height=100,
                                fit=ft.ImageFit.CONTAIN
                            )
                        ),
                        Divider(),

                        Text("Login", style = AppConfig.get_text_style(page, "title_large")),
                        identificacao_field,
                        senha_field,
                        login_button,
                        Row(
                            [
                                Text("Esqueci minha senha", style = AppConfig.get_text_style(page, "body_small")),
                                Text("Cadastrar", style = AppConfig.get_text_style(page, "body_small"))
                            ],
                            
                            alignment="center"
                        ),
                        
                    ],
                    horizontal_alignment="center",
                    alignment="center",
                    spacing=30,
                    width=600,
                    expand=True
                    
                    
                ),
                
                expand=False,
                alignment=ft.alignment.center,
                
                
            )
        ],
        padding=40,
        spacing=0,
        vertical_alignment="center",
        horizontal_alignment="center",
        bgcolor=AppConfig.COLOR_PALETTE["background"],
        
        
    )
