import flet as ft

import flet as ft
from flet import Page, View, Column, Row, Container, Divider, AlertDialog, Stack
from flet import Text, ElevatedButton, TextField, TextButton

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
            )
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
        espaco = Container(expand=True)

        if header:
            conteudo.append(self._build_header())

        if body:
            conteudo.append(espaco)
            conteudo.append(body)
            conteudo.append(espaco)

        if footer:
            conteudo.append(self._build_footer())

        return Container(
            content=Column(
                controls=conteudo,
                expand=True,
                spacing=20,
            ),
            expand=True,
            padding=20
        )


class aviso():
    """ Classe para mostrar diálogos de aviso """
    def __init__(self, page: Page, titulo: str, texto: str | Exception):
        self.page = page

        self.dialog = AlertDialog(
            modal=True,
            on_dismiss= lambda _: self.close_dialog(),  # <-- fecha o diálogo

            title=Row(
                        [
                            
                            ft.Text(
                                titulo,
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color="#FFFFFF",
                                text_align=ft.TextAlign.CENTER,
                                expand=True
                            ),
                            ft.IconButton(
                                alignment=ft.alignment.top_left,
                                icon=ft.Icons.CLOSE,
                                bgcolor="#5C5C5C",
                                icon_color="white",
                                on_click= lambda _: self.close_dialog(),
                            ),
                           
                        ],
                        
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
            
            content=Column(
                [
                    
                    Container(expand=True),
                    Text(
                        str(texto),
                        size=16,
                        color="#FFFFFF",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    Container(expand=True),
                    ElevatedButton(
                        "CONFIRMAR",
                        width=183,
                        height=51,
                        style=ft.ButtonStyle(
                            bgcolor="#5C5C5C",
                            color="#F5F9FC",
                            overlay_color="#212529",
                            padding=ft.padding.symmetric(horizontal=20, vertical=10),
                            shape=ft.RoundedRectangleBorder(radius=1),
                            side=ft.BorderSide(color=ft.Colors.WHITE, width=1)
                        ),
                        on_click= lambda _: self.close_dialog()
                    ),
                ],
                height=207,
                width=378,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor="#363636",
            content_padding=ft.padding.all(15),
        )

        self.show()

    def show(self):
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def close_dialog(self):
        self.dialog.open = False
        self.page.update()


    # def buttons(self, *buttons):
    #     for button in buttons:
    #         self.dialog.actions.append(button)