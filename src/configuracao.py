# import flet as ft
# from flet import Page




# def configurar_mobile(page: Page):
#         """Configurações específicas para dispositivos móveis"""
#         page.window_full_screen = True  # Tela cheia em mobile

#         page.theme = ft.Theme(

#             color_scheme=ft.ColorScheme(
#                 primary="#1E49C0",
#                 secondary="#1469A1",
#                 tertiary="#1469A1",
#                 error="#1469A1",
                
#                 on_primary="#1469A1",
#                 on_secondary="#1469A1",
#                 on_tertiary="#1469A1",
#                 on_error="#1469A1",
#             ),

#             text_theme=ft.TextTheme(
#                                     body_large=ft.TextStyle(size=16, color="#B5E0FD"),
#                                     body_medium=ft.TextStyle(size=14, color="#B5E0FD"), # Texto
#                                     body_small=ft.TextStyle(size=12, color="#B5E0FD"),

#                                     title_large=ft.TextStyle(size=24, color="#B5E0FD", weight=ft.FontWeight.BOLD,), # Títulos
#                                     title_medium=ft.TextStyle(size=20, color="#B5E0FD",  weight=ft.FontWeight.BOLD,),
#                                 ),

#             elevated_button_theme=ft.ElevatedButtonTheme(
#                                     color="#F5F9FC",                  # Cor do texto
#                                     bgcolor="#1469A1",                # Cor de fundo
#                                     overlay_color="#1E88E5",          # Cor quando hover
#                                     shadow_color="#0D47A1",           # Cor da sombra
#                                     elevation=4,                      # Altura da sombra
#                                     padding=ft.padding.symmetric(horizontal=20, vertical=15),  # Espaçamento interno
#                                     shape=ft.RoundedRectangleBorder(radius=10),  # Bordas arredondadas
#                                     animation_duration=200,           # Duração da animação
#                                 ),
            
#         )

#         page.padding = 10  # Menos padding em telas pequenas

# def configurar_web(page: Page):
#     """Configurações específicas para web"""
#     page.window.width = 1024
#     page.window.height = 768

#     page.window.resizable = True
#     page.theme = ft.Theme(
#         text_theme=ft.TextTheme(
#                                 body_large=ft.TextStyle(size=18, color="#B5E0FD"),
#                                 body_medium=ft.TextStyle(size=16, color="#B5E0FD"), # Texto
#                                 body_small=ft.TextStyle(size=14, color="#B5E0FD"),

#                                 title_large=ft.TextStyle(size=44, color="#B5E0FD", weight=ft.FontWeight.BOLD,), # Títulos
#                                 title_medium=ft.TextStyle(size=24, color="#B5E0FD",  weight=ft.FontWeight.BOLD,),
#                             ),

#         elevated_button_theme=ft.ElevatedButtonTheme(
#                                 color="#F5F9FC",                  # Cor do texto
#                                 bgcolor="#1469A1",                # Cor de fundo
#                                 overlay_color="#1E88E5",          # Cor quando hover
#                                 shadow_color="#0D47A1",           # Cor da sombra
#                                 elevation=4,                      # Altura da sombra
#                                 padding=ft.padding.symmetric(horizontal=20, vertical=15),  # Espaçamento interno
#                                 shape=ft.RoundedRectangleBorder(radius=10),  # Bordas arredondadas
#                                 animation_duration=200,           # Duração da animação
#                             ),
#     )

#     page.padding = 10

# def configurar_desktop(page: Page):
#     """Configurações específicas para desktop"""
#     page.window.width = 1024
#     page.window.height = 768
#     page.window.min_width = 800
#     page.window.min_height = 600
#     page.theme = ft.Theme(
#         # Configurações de tema para desktop
#     )

# # Configurações baseadas na plataforma
# if page.platform in ["android", "ios"]:
#     # Configurações para mobile
#     page.title = "Sistema de Votação Mobile"
#     configurar_mobile(page)
# elif page.platform == "web":
#     # Configurações para web
#     page.title = "Sistema de Votação Web"
#     configurar_web(page)
# else:
#     # Configurações para desktop (windows, macos, linux)
#     page.title = "Sistema de Votação Desktop"
#     configurar_desktop(page)