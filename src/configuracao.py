import flet as ft
from flet import Page, Theme, TextStyle, FontWeight, padding, RoundedRectangleBorder, ButtonStyle

class AppConfig:
    """Classe para configurações da aplicação"""
    
    # Paleta de cores consistente
    COLOR_PALETTE = {
        "button_primary": "#CF0810",
        "button_on_hover": "#800408",
        "secondary": "#1469A1",
        
        "accent": "#B3B3B3",
        "text": "#ffffff",

        "background": "#212327",
        "surface": "#212327",

        "error": "#FF6B6B",
        "success": "#4CAF50",
        
        "teste": "#2FCB34",
        "teste_2": "#CB732F",
        "teste_3": "#2F9CCB",
        "teste_4": "#CB2F82"
    }

    @staticmethod
    def get_theme_config(page_platform):
        """Retorna configurações de tema baseadas na plataforma"""
        is_mobile = page_platform in ["android", "ios"]
        
        return {
            "text_sizes": {
                "title_large": 32 if is_mobile else 48,
                "title_medium": 24 if is_mobile else 32,
                "title_small": 20 if is_mobile else 24,
                "body_large": 16 if is_mobile else 20,
                "body_medium": 14 if is_mobile else 16,
                "body_small": 12 if is_mobile else 14,
                "label": 14 if is_mobile else 18
            },
            "spacing": {
                "small": 8 if is_mobile else 12,
                "medium": 16 if is_mobile else 24,
                "large": 24 if is_mobile else 32,
                "xlarge": 32 if is_mobile else 48
            },
            "padding": {
                "small": padding.symmetric(horizontal=8, vertical=8),
                "medium": padding.symmetric(horizontal=12, vertical=12),
                "large": padding.symmetric(horizontal=16, vertical=16)
            },
            "button": {
                "min_width": 120 if is_mobile else 160,
                "padding": padding.symmetric(
                    horizontal=16 if is_mobile else 24,
                    vertical=12 if is_mobile else 16
                )
            }
        }

    @staticmethod
    def get_text_field_style(page: Page):
        """Retorna o estilo para TextField baseado na plataforma"""
        is_mobile = page.platform in ["android", "ios"]
        colors = AppConfig.COLOR_PALETTE
        
        return {
            "border_color": colors["secondary"],
            "border" :ft.InputBorder.UNDERLINE,
            "focused_border_color": colors["accent"],
            "cursor_color": colors["accent"],
            "text_size": 16 if not is_mobile else 14,
            "color": colors["text"],
            "bgcolor": colors["surface"],
            "border_radius": 8,
            "border_width": 1.5,
            "content_padding": padding.symmetric(
                horizontal=12 if is_mobile else 16,
                vertical=14 if is_mobile else 16
            ),
            "label_style": TextStyle(color=colors["accent"], size=14 if is_mobile else 16)
        }
    
    @staticmethod
    def get_text_style(page: Page, style_type: str):
        """Retorna o estilo de texto baseado na plataforma"""
        theme_config = AppConfig.get_theme_config(page.platform)
        colors = AppConfig.COLOR_PALETTE
        
        styles = {
            "title_large": TextStyle(
                size=theme_config["text_sizes"]["title_large"],
                weight=FontWeight.BOLD,
                color=colors["text"]
            ),
            "title_medium": TextStyle(
                size=theme_config["text_sizes"]["title_medium"],
                weight=FontWeight.BOLD,
                color=colors["text"]
            ),
            "title_small": TextStyle(
                size=theme_config["text_sizes"]["title_small"],
                weight=FontWeight.BOLD,
                color=colors["text"]
            ),
            "body_medium": TextStyle(
                size=theme_config["text_sizes"]["body_medium"],
                color=colors["text"]
            ),
            "body_small": TextStyle(
                size=theme_config["text_sizes"]["body_small"],
                color=colors["text"]
            ),
            "body_description": TextStyle(
                size=theme_config["text_sizes"]["body_small"],
                color=colors["accent"]
            ),
            "label": TextStyle(
                size=theme_config["text_sizes"]["label"],
                color=colors["text"]
            )
        }
        
        return styles.get(style_type, styles["body_medium"])

    @staticmethod
    def get_elevated_button_style(page: Page):
        """Retorna estilo para ElevatedButton baseado na plataforma"""
        colors = AppConfig.COLOR_PALETTE
        theme_config = AppConfig.get_theme_config(page.platform)
        
        return ButtonStyle(
        bgcolor=colors["button_primary"],
        color=colors["text"],
        elevation=4,
        padding=theme_config["button"]["padding"],
        shape=RoundedRectangleBorder(radius=8),
        overlay_color=colors["button_on_hover"]
    )

def configurar_app(page: Page):
    """Configura a aplicação baseada na plataforma"""
    
    # Configurações de janela
    if page.platform in ["android", "ios"]:
        configurar_mobile(page)
    elif page.platform == "web":
        configurar_web(page)
    else:
        configurar_desktop(page)
    
    # Aplicar tema global
    aplicar_tema_global(page)

def configurar_mobile(page: Page):
    """Configurações específicas para mobile"""
    print("Configurando mobile")
    page.window.full_screen = True
    page.title = "Sistema de Votação Mobile"
    page.padding = 10
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

def configurar_web(page: Page):
    """Configurações específicas para web"""
    print("Configurando web")
    page.window.width = 1024
    page.window.height = 768
    page.window.resizable = True
    page.title = "Sistema de Votação Web"
    page.padding = 20

def configurar_desktop(page: Page):
    """Configurações específicas para desktop"""
    # print("Configurando desktop")
    page.window.width = 1024
    page.window.height = 768
    page.window.min_width = 800
    page.window.min_height = 600
    page.title = "Sistema de Votação Desktop"
    page.padding = 20
    page.window.center()

def aplicar_tema_global(page: Page):
    """Aplica o tema global baseado na plataforma"""
    theme_config = AppConfig.get_theme_config(page.platform)
    colors = AppConfig.COLOR_PALETTE
    
    page.theme = Theme(
        color_scheme=ft.ColorScheme(
            primary=colors["button_primary"],
            on_primary=colors["button_on_hover"],

            secondary=colors["secondary"],
            on_secondary=colors["text"],
            
            error=colors["error"],
            on_error=colors["text"],
            
            background=colors["background"],
            on_background=colors["text"],

            surface=colors["surface"],
            on_surface=colors["text"],
            
        ),
        text_theme=ft.TextTheme(
            title_large=TextStyle(
                size=theme_config["text_sizes"]["title_large"],
                weight=FontWeight.BOLD,
                color=colors["text"]
            ),
            title_medium=TextStyle(
                size=theme_config["text_sizes"]["title_medium"],
                weight=FontWeight.BOLD,
                color=colors["text"]
            ),
            title_small=TextStyle(
                size=theme_config["text_sizes"]["title_small"],
                weight=FontWeight.BOLD,
                color=colors["text"]
            ),
            body_large=TextStyle(
                size=theme_config["text_sizes"]["body_large"],
                color=colors["text"]
            ),
            body_medium=TextStyle(
                size=theme_config["text_sizes"]["body_medium"],
                color=colors["text"]
            ),
            label_large=TextStyle(
                size=theme_config["text_sizes"]["label"],
                color=colors["text"]
            )
        )
    )
    page.theme_mode = "dark"  # Forçar tema escuro