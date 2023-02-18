import pygame, sys

from Gamable import Gamable
from GameState import GameState
from constants import *

class AudioSettingsMenu(Gamable):
    def __init__(self) -> None:
        self.optionIndex = 0
        self.volume = 2
        self.font = pygame.font.SysFont('msgothic', 16)
        self.back_option = self.font.render('戻る', True, (255, 255, 255))
        self.volume_width = 32
        self.volume_height = 4
        
    def update(self, change_game_state) -> str:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.optionIndex -= 1
                elif event.key == pygame.K_s:
                    self.optionIndex += 1
                if event.key == pygame.K_a:
                    self.volume -= 2
                elif event.key == pygame.K_d:
                    self.volume += 2
                
                if event.key == pygame.K_RETURN:
                    if self.optionIndex == 1:
                        change_game_state(GameState.SettingsMenu)
            if self.volume >= self.volume_width:
                self.volume = self.volume_width
            if self.volume < 0:
                self.volume = 0
        
        return 'AudioSettings'

    def draw(self, surface):
        x = (WIDTH - self.volume_width) / 2 * BLOCK
        y = (HEIGHT - self.volume_height) / 2 * BLOCK
        pygame.draw.rect(surface, (255, 255, 255), (x, y, self.volume_width*BLOCK, self.volume_height*BLOCK ), 1, 0)
        surface.fill( (255, 255, 255), (x, y, self.volume*BLOCK, self.volume_height*BLOCK))

        y2 = HEIGHT / 2 * BLOCK
        x2 = WIDTH / 2 * BLOCK
        surface.blit(self.back_option, (x2, y2+BLOCK*6))
        if self.optionIndex == 0:
            surface.blit(self.font.render('.(☞ﾟヮﾟ)☞', True, (255, 255, 255)), (x-BLOCK*7, y+self.volume_height/2*BLOCK))
        if self.optionIndex == 1:
            surface.blit(self.font.render('.(☞ﾟヮﾟ)☞', True, (255, 255, 255)), (x2-BLOCK*7, y2+BLOCK*6))


