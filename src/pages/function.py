import flet as ft
from flet import Page, Text, AlertDialog, TextButton


class LettersOnlyInputFilter(ft.InputFilter):
    """ Filtro para permitir apenas letras e espaços no TextField """
    def __init__(self):
        super().__init__(regex_string=r"[a-zA-ZáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇàèìòùÀÈÌÒÙäëïöüÄËÏÖÜñÑ\s'-]")
        
    def filter(self, text, multiline=False):
        import re
        return re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇàèìòùÀÈÌÒÙäëïöüÄËÏÖÜñÑ\s\'- ]', '', text)
    

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
            bgcolor="#1469A1",  # Cor de fundo do diálogo
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



text_field_style = {
    "border_color": "#85ACC7",  # Cor da borda
    "border_radius": 10,        # Cantos arredondados
    "border_width": 1.5,        # Espessura da borda
    "focused_border_color": "#207FBE",  # Cor quando em foco
    "cursor_color": "#1469A1",  # Cor do cursor
    "selection_color": "#B5E0FD",  # Cor da seleção de texto
    "text_size": 16,            # Tamanho do texto
    "color": "#B5E0FD",         # Cor do texto digitado
    "bgcolor": "#000000",       # Cor de fundo
    "height": 50,               # Altura consistente
    "content_padding": 15       # Espaçamento interno
}

elevated_button_style = ft.ButtonStyle(
    color="#F5F9FC",                  # Cor do texto
    bgcolor="#1469A1",                # Cor de fundo
    overlay_color="#1E88E5",          # Cor quando hover
    shadow_color="#0D47A1",           # Cor da sombra
    elevation=4,                      # Altura da sombra
    padding=ft.padding.symmetric(horizontal=20, vertical=15),  # Espaçamento interno
    shape=ft.RoundedRectangleBorder(radius=10),  # Bordas arredondadas
    animation_duration=200,           # Duração da animação
)