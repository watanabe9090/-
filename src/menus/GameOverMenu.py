import pygame, sys
from Gamable import Gamable
from GameState import GameState
from constants import *


class GameOverMenu(Gamable):
    def __init__(self) -> None:
        self.title_font = pygame.font.SysFont('msgothic', 64)
        self.subtitle_font = pygame.font.SysFont('msgothic', 32)

        self.title = self.title_font.render('ゲームオーバー', True, WHITE)
        self.subtitle = self.subtitle_font.render('エンターボタンを押して... (；′⌒`)', True, WHITE)

        self.frame = 0
        self.blink_frame = 30
        self.move_frame = 10
        self.apper = True

        self.snake_x = 10
        self.snake_y = 10

    def update(self, change_game_state) -> str:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    change_game_state(GameState.MainMenu)
        self.frame+=1
        if self.frame >= self.blink_frame:
            self.frame = 0
            self.apper = not self.apper
        if self.frame % self.move_frame:
            pass

    def draw(self, surface):
        x = (WIDTH*BLOCK - self.title.get_width()) / 2 
        y = (HEIGHT*BLOCK - self.title.get_height()) / 2 
        x2 = (WIDTH*BLOCK - self.subtitle.get_width()) / 2 
        y2 = (HEIGHT*BLOCK - self.subtitle.get_height()) / 2 + BLOCK*8 
        if self.apper:
            surface.blit(self.title, (x, y))
        surface.blit(self.subtitle, (x2, y2))