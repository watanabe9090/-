import pygame, sys

from Gamable import Gamable
from GameState import GameState
from constants import *

class SettingsMenu(Gamable):
    def __init__(self) -> None:
        self.optionIndex = 0
        self.font = pygame.font.SysFont('msgothic', 16)
        self.options = [
            self.font.render('音量', True, (255, 255, 255)),
            self.font.render('戻る', True, (255, 255, 255))
        ]
        
    def update(self, change_game_state) -> str:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.optionIndex -= 1
                elif event.key == pygame.K_s:
                    self.optionIndex += 1
                if event.key == pygame.K_RETURN:
                    if self.optionIndex == 0:
                        change_game_state(GameState.AudioSettingsMenu)
                    elif self.optionIndex == 1:
                        change_game_state(GameState.MainMenu)
        
        if self.optionIndex >= len(self.options):
            self.optionIndex = 0
        if self.optionIndex < 0:
            self.optionIndex = len(self.options)-1
        return 'Settings'

    def draw(self, surface):
        mid_x = BLOCK*WIDTH/2
        mid_y = BLOCK*HEIGHT/2;
        for index, option in enumerate(self.options):
            y = mid_y+index*BLOCK*2
            if index == self.optionIndex:
                surface.blit(self.font.render('.(☞ﾟヮﾟ)☞', True, (255, 255, 255)), (mid_x-120, y))
            surface.blit(option, (mid_x, y))

