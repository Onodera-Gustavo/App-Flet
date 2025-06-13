import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField

from pages.function import aviso
from configuracao import AppConfig

def tela_menu(page: Page):

    AppConfig.get_elevated_button_style(page)

    cadastrar_button = ft.Stack(
        controls=[
            ft.Container(
                width=180,
                height=61, 
                bgcolor=AppConfig.COLOR_PALETTE["error"],
                        border_radius=ft.border_radius.only(
                        top_left=0,
                        top_right=0,
                        bottom_left=30,
                        bottom_right=0)
            ),
            ft.Container(
                width=40,
                height=61,
                bgcolor=AppConfig.COLOR_PALETTE["error"],
                left=10,
                top=1,
                rotate=ft.Rotate(angle=44.8),
            ),
            ft.Text("Menu", left=50, top=18)
        ]
    )

    editar_button = ElevatedButton(
        text="Editar",
        scale=1.2,
        width=250,
        # on_click=lambda _: page.go(/"editar"),
        style= AppConfig.get_elevated_button_style(page, style_type="menu")
    )

    relatorios_button = ElevatedButton(
        text="Relatório",
        scale=1.2,
        width=250,
        # on_click=lambda _: page.go("/relatorio"),
        style= AppConfig.get_elevated_button_style(page, style_type="menu")
    )

    finalizar_button = ElevatedButton(
        text="Finalizar Sessão",
        scale=1.2,
        width=250,
        on_click=lambda _: page.go("/"),
        style= AppConfig.get_elevated_button_style(page, style_type="menu")
    )

    def finalizar_secao():
        """Encerra a sessão do usuário"""
        #para retornar ao login
        page.go("/")

    # Menu para o Administrador 
    return View(
        route="/menu",
        controls=[
            Container(
                expand = True,
                # bgcolor=AppConfig.COLOR_PALETTE["teste"],
                content=Column(
                    [
                        Container(
                            # bgcolor=AppConfig.COLOR_PALETTE["teste_2"],
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
                        Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["success"]),
                        Row(
                            [
                                Container(
                                    width=600,
                                    content=Column(
                                        [
                                            Row(
                                                    [
                                                        cadastrar_button,
                                                        editar_button,
                                                    ],
                                                    alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                                                    spacing=50
                                                ),
                                            Container(
                                                # bgcolor=AppConfig.COLOR_PALETTE["teste_3"],
                                                content=Column(
                                                    [
                                                        ft.Image(
                                                            src="../assets/Logo.png",
                                                            width=100,
                                                            height=100,
                                                            fit=ft.ImageFit.CONTAIN
                                                        )
                                                    ],
                                                ),
                                                
                                            ),
                                            Row(
                                                [
                                                    relatorios_button,
                                                    finalizar_button,
                                                ],
                                                alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                                                spacing=50
                                            )
                                        ],
                                        alignment= ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment="center",
                                        spacing=20
                                    )
                                ), 
                               
                            ],
                            alignment= ft.MainAxisAlignment.CENTER,
                            height=400
                        ),
                        
                        Container(expand=True, bgcolor=AppConfig.COLOR_PALETTE["success"]),
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
                    ]
                )

            )#Container 
        ],#Control
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],  
    )

