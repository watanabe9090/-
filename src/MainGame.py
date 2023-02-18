import pygame, sys, random

from Gamable import Gamable
from GameState import GameState
from IO.InputMaster import InputMaster
from IO.FontManager import FontManager
from constants import *

from game_objects.Kanji import Kanji

class MainGame(Gamable):
    def __init__(self, snake, kanji, points) -> None:
        super().__init__()
        self.font = FontManager.get_font(font_size=16)
        self.grid_color = (71, 71, 71)
        self.snake = snake
        self.kanji = kanji
        self.points = points
        self.frame = 0
        self.max_frame = 5
        self.input_master = InputMaster()
        

    def update(self, change_game_state) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        self.input_master.poll()
        self.snake.direction = self.input_master.direction

        if(self.frame >= self.max_frame):
            self.update_on_frame(change_game_state)
            self.frame = 0

        self.frame+=1

    def draw(self, surface):
        self.snake.draw(surface)
        self.kanji.draw(surface)
        for i in range(HEIGHT+1):
            p1 = (0, i*BLOCK)
            p2 = (WIDTH*BLOCK, i*BLOCK)
            pygame.draw.line(surface, self.grid_color, p1, p2, 1)
        for i in range(WIDTH+1):
            p1 = (i*BLOCK, 0)
            p2 = (i*BLOCK, HEIGHT*BLOCK)
            pygame.draw.line(surface, self.grid_color, p1, p2, 1)
        points_text = self.font.render('点数:', True, WHITE)
        points_text_pos = (BLOCK*2,HEIGHT*BLOCK + MENU_HEIGHT*BLOCK*(2/3))
        points_value = self.font.render(str(self.points), True, WHITE)
        points_value_pos = (BLOCK*6,HEIGHT*BLOCK + MENU_HEIGHT*BLOCK*(2/3))
        surface.blit(points_text, points_text_pos)
        surface.blit(points_value, points_value_pos)
            

    def update_on_frame(self, change_game_state):
        self.snake.update()
        if self.snake.x >= WIDTH*BLOCK or self.snake.x < 0 or self.snake.y >= HEIGHT*BLOCK or self.snake.y < 0 or self.snake.is_self_colisioned():
            change_game_state(GameState.GameOver)
        if self.kanji.is_colided(self.snake.x, self.snake.y):
            x = random.randint(0, WIDTH-1)
            y = random.randint(0, HEIGHT-1)
            self.kanji = Kanji(BLOCK*x, BLOCK*y)
            self.points += 10
            self.snake.add_piece()




