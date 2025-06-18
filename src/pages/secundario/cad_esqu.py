import flet as ft
from flet import Page, View, Column, Row, Container, Divider, GridView
from flet import Text, ElevatedButton, TextField

from pages.function import aviso, TelaBase
from configuracao import AppConfig

def tela_cad_esqu(page: Page):
    tela = TelaBase(page)
    
    text_field_style = AppConfig.get_text_field_style(page)

    body = Container(
        alignment=ft.alignment.center,
        
        content=Column(
            [   
                Text("Cadastrar", text_align="center" ,style=AppConfig.get_text_style(page, style_type="title_medium")),
                Column(
                    [
                        TextField(label="Identificação", width=360, prefix_icon=ft.Icons.PERSON, autofocus=True, **text_field_style),
                        TextField(label="Senha",width=360, prefix_icon=ft.Icons.LOCK, **text_field_style, password=True, can_reveal_password=True),
                        TextField(label="Confirme sua senha",width=360, prefix_icon=ft.Icons.LOCK, **text_field_style, password=True, can_reveal_password=True)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                Row(
                    [
                        ElevatedButton("Cadastrar", scale=1.3, on_click=lambda _: page.go("/"), style=AppConfig.get_elevated_button_style(page)),
                        ElevatedButton("Retornar", scale=1.3, on_click=lambda _: page.go("/"), style=AppConfig.get_elevated_button_style(page)),
                    ],
                    width=450,
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                )
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    return View(
        route="/cad_esqu", 
        controls=[tela.construir(body)],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        
    )
    