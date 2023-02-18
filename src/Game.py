import pygame, sys

from constants import *
from GameState import GameState
from MainGame import MainGame

from menus.MainMenu import MainMenu
from menus.SettingsMenu import SettingsMenu
from menus.GameOverMenu import GameOverMenu
from menus.AudioSettingsMenu import AudioSettingsMenu
from game_objects.Snake import Snake
from game_objects.Kanji import Kanji

class Game:
    def __init__(self) -> None:
        self.running = False
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('msgothic', 16)
        self.resolution = (BLOCK*WIDTH+1, BLOCK*HEIGHT+1+MENU_HEIGHT*BLOCK)
        self.screen = pygame.display.set_mode(self.resolution)
        self.game_level = None

        self.points = 0
        self.kanji = Kanji(64, 64)
        self.snake = Snake()

        pygame.display.set_caption('蛇食字')

    def start(self):
        self.running = True
        self.game_level = MainMenu()
        self.mainloop()
    
    def reset(self) -> None:
        self.points = 0
        self.kanji = Kanji(64, 64)
        self.snake = Snake()

    def change_game_state(self, game_state):
        if game_state == GameState.Running and self.game_level != GameState.Paused:
            self.reset()
            self.game_level = MainGame(self.snake, self.kanji, self.points)
        elif game_state == GameState.Paused:
            pass
        elif game_state == GameState.MainMenu:
            self.game_level = MainMenu()
        elif game_state == GameState.SettingsMenu:
            self.game_level = SettingsMenu()
        elif game_state == GameState.AudioSettingsMenu:
            self.game_level = AudioSettingsMenu()
        elif game_state == GameState.GameOver:
            self.game_level = GameOverMenu()
        elif game_state == GameState.Exited:
            pygame.quit()
            sys.exit(0)

    def mainloop(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.game_level.update(self.change_game_state)
            self.game_level.draw(self.screen)
            self.clock.tick(60)
            pygame.display.flip()

    