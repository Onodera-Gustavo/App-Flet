import flet as ft
from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField

from pages.function import aviso
from configuracao import AppConfig

def tela_menu(page: Page):

    AppConfig.get_elevated_button_style(page)

    def on_hover(e: ft.HoverEvent):
        e.control.opacity = 0.65 if e.data == "true" else 1.0
        e.control.update()

    # Corte inferior esquerdo, Page.go_Editar
    editar_button = ft.Container(
        shadow=[
            ft.BoxShadow(
                blur_radius=12,
                color=ft.Colors.BLACK26,
                offset=ft.Offset(6, 6),
                spread_radius=1,
            )
        ],
        on_click=lambda _: page.go("/edicao"),
        
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=180,
                    height=67,
                    bgcolor= AppConfig.COLOR_PALETTE["on_primary"],
                    border_radius=ft.border_radius.only(
                        bottom_left=30
                    )
                ),
                ft.Container(
                    width=40,
                    height=67,
                    bgcolor= AppConfig.COLOR_PALETTE["on_primary"],
                    left=10,
                    top=1,
                    
                    rotate=ft.Rotate(angle=44.8),
                ),
                ft.Text("Editar", left=40, top=18, style=AppConfig.get_text_style(page, "body_large"))
            ]
        ),
        on_hover=on_hover,
        animate_opacity=200,
    )

    # Corte inferior direito, Page.go_Cadastro
    cadastrar_button = ft.Container(
        shadow=[
            ft.BoxShadow(
                blur_radius=12,
                color=ft.Colors.BLACK26,
                offset=ft.Offset(6, 6),
                spread_radius=1,
            )
        ],
        on_click= lambda _: page.go("/cadastro"),
        
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=180,
                    height=67,
                    bgcolor= AppConfig.COLOR_PALETTE["on_primary"],
                    border_radius=ft.border_radius.only(
                        bottom_right=30
                    )
                ),
                ft.Container(
                    width=40,
                    height=67,
                    bgcolor= AppConfig.COLOR_PALETTE["on_primary"],
                    left=130,
                    top=1,
                    rotate=ft.Rotate(angle=-44.8),
                ),
                ft.Text("Cadastrar", left=40, top=18, style=AppConfig.get_text_style(page, "body_large"))
            ]
        ),
        on_hover=on_hover,
        animate_opacity=200,
    )

    # Corte superior esquerdo, Page.go_Relatorios
    relatorios_button = ft.Container(
        shadow=[
            ft.BoxShadow(
                blur_radius=12,
                color=ft.Colors.BLACK26,
                offset=ft.Offset(6, 6),
                spread_radius=1,
            )
        ],
        on_click = lambda _: page.go("/relatorio"),
        
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=180,
                    height=67,
                    bgcolor= AppConfig.COLOR_PALETTE["on_primary"],
                    border_radius=ft.border_radius.only(
                        top_left=30,
                    )
                ),
                ft.Container(
                    width=40,
                    height=67,
                    bgcolor= AppConfig.COLOR_PALETTE["on_primary"],
                    left=10,
                    top=1,
                    rotate=ft.Rotate(angle=-44.8),
                ),
                ft.Text("Relatórios", left=40, top=18, style=AppConfig.get_text_style(page, "body_large"))
            ]
        ),
        on_hover=on_hover,
        animate_opacity=200,
    )
    
    # Corte superior direito, Page.go_Login 
    finalizar_button = ft.Container(
        shadow=[
            ft.BoxShadow(
                blur_radius=12,
                color=ft.Colors.BLACK26,
                offset=ft.Offset(6, 6),
                spread_radius=1,
            ),
        ],
        on_click=lambda _: page.go("/"),
        
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=180,
                    height=67,
                   bgcolor= AppConfig.COLOR_PALETTE["on_primary"],
                    border_radius=ft.border_radius.only(
                        top_right=30
                    )
                ),
                ft.Container(
                    width=40,
                    height=67,
                   bgcolor= AppConfig.COLOR_PALETTE["on_primary"],
                    left=130,
                    top=1,
                    rotate=ft.Rotate(angle=44.8),
                ),
                ft.Text("Finalizar", left=40, top=18, style=AppConfig.get_text_style(page, "body_large"))
            ]
        ),
        on_hover=on_hover,
        animate_opacity=200,
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
                        Container(expand=True),
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
                                                    spacing=10
                                                ),
                                            Container(
                                                # bgcolor=AppConfig.COLOR_PALETTE["teste_3"],
                                                content=Column(
                                                    [
                                                        ft.Image(
                                                            src="../assets/icon.png",
                                                            width=100,
                                                            height=100,
                                                            fit=ft.ImageFit.CONTAIN
                                                        )
                                                    ],
                                                ),
                                                
                                            ),
                                            Row(
                                                [
                                                    finalizar_button,
                                                    relatorios_button,
                                                    
                                                ],
                                                alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                                                spacing=10
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
                    ]
                )

            )#Container 
        ],#Control
        padding=20,
        spacing=0,
        bgcolor=AppConfig.COLOR_PALETTE["background"],  
    )

