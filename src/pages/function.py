import flet as ft

from flet import Page, View, Column, Row, Container, Divider
from flet import Text, ElevatedButton, TextField, TextButton, AlertDialog

from configuracao import AppConfig

import flet as ft
from flet import Page, Container, Column, Row, Text, Divider, Image

class TelaBase:
    def __init__(self, page: Page):
        self.page = page

    def _build_header(self) -> Container:
        return Container(
            alignment=ft.alignment.top_center,
            content=Column(
                [
                    Image(
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
        )

    def _build_footer(self) -> Container:
        return Container(
            content=Column(
                [
                    Row(
                        [
                            Text("Termos de uso", style=AppConfig.get_text_style(self.page, style_type="body_description")),
                            Text("|", style=AppConfig.get_text_style(self.page, style_type="body_description")),
                            Text("Política de privacidade", style=AppConfig.get_text_style(self.page, style_type="body_description")),
                            Text("|", style=AppConfig.get_text_style(self.page, style_type="body_description")),
                            Text("Cookies", style=AppConfig.get_text_style(self.page, style_type="body_description"))
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND
                    ),
                    Divider(color=AppConfig.COLOR_PALETTE["accent"], height=1),
                    Row(
                        [
                            Text("SENAI - SP", style=AppConfig.get_text_style(self.page, style_type="body_description")),
                            Text("|", style=AppConfig.get_text_style(self.page, style_type="body_description")),
                            Text("Game Awards", style=AppConfig.get_text_style(self.page, style_type="body_description"))
                        ],
                        alignment=ft.MainAxisAlignment.START
                    )
                ],
                spacing=4,
            )
        )

    def construir(self, body: Container, header: bool = True, footer: bool = True) -> Container:
        conteudo = []

        if header:
            conteudo.append(self._build_header())

        if body:
            conteudo.append(body)

        if footer:
            conteudo.append(self._build_footer())

        return Container(
            content=Column(
                controls=conteudo,
                expand=True,
                spacing=20,
            ),
            padding=20
        )


class aviso():
    """ Classe para mostrar diálogos de aviso """
    def __init__(self, page: Page, titulo: str, texto: str|Exception):
        self.page = page
        
        self.dialog = AlertDialog(
            modal=True,
            title= Text(
                titulo,
                size=20,
                weight=ft.FontWeight.BOLD,
                color="#F5F9FC" 
            ),
            content= Text(
                str(texto),
                size=16,
                color="#B5E0FD" 
            ),
            actions=[
                TextButton(
                    "OK",
                    style=ft.ButtonStyle(
                        color="#F5F9FC",
                        overlay_color="#1E88E5",
                        padding=ft.padding.symmetric(horizontal=20, vertical=10)),
                    on_click=self.close_dialog
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            shape=ft.RoundedRectangleBorder(radius=10),  # Bordas arredondadas
            bgcolor="#1469A1",
            content_padding=ft.padding.all(20),  # Espaçamento interno
        )
        
        self.show()

    def show(self):
        self.page.overlay.append(self.dialog) # Adiciona o diálogo aos overlays para aparecer afrente da página
        self.page.update()
        self.dialog.open = True
        self.page.update()

    def close_dialog(self, e=None):
        self.dialog.open = False
        self.page.update()

    # def buttons(self, *buttons):
    #     for button in buttons:
    #         self.dialog.actions.append(button)