import pygame

pygame.font.init()

class FontManager:
    avaliable_font_names = pygame.font.get_fonts()
    font_name = 'notosanscjkjp'#avaliable_font_names[0]

    def get_font(font_name: str = font_name, font_size: int = 16):
        return pygame.font.SysFont(FontManager.font_name, font_size)




