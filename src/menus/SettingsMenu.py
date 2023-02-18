import pygame, sys

from Gamable import Gamable
from GameState import GameState
from IO.FontManager import FontManager
from constants import *

class SettingsMenu(Gamable):
    def __init__(self) -> None:
        self.option_index = 0
        # self.font = pygame.font.SysFont('msgothic', 16)
        self.font = FontManager.get_font()
        self.options = [
            self.font.render('音量', True, WHITE),
            self.font.render('Font', True, WHITE),
            self.font.render('戻る', True, WHITE)
        ]
        
    def update(self, change_game_state) -> str:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.option_index -= 1
                elif event.key == pygame.K_s:
                    self.option_index += 1
                if event.key == pygame.K_RETURN:
                    if self.option_index == 0:
                        change_game_state(GameState.AudioSettingsMenu)
                    elif self.option_index == 1:
                        change_game_state(GameState.FontSettingsMenu)
                    elif self.option_index == 2:
                        change_game_state(GameState.MainMenu)
        
        if self.option_index >= len(self.options):
            self.option_index = 0
        if self.option_index < 0:
            self.option_index = len(self.options)-1

    def draw(self, surface):
        mid_x = BLOCK*WIDTH/2
        mid_y = BLOCK*HEIGHT/2
        for index, option in enumerate(self.options):
            y = mid_y+index*BLOCK*2
            if index == self.option_index:
                surface.blit(self.font.render('.(☞ﾟヮﾟ)☞', True, (255, 255, 255)), (mid_x-120, y))
            surface.blit(option, (mid_x, y))

