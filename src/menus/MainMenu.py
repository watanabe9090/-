import pygame, sys, random

from Gamable import Gamable
from GameState import GameState
from IO.InputMaster import InputState
from IO.FontManager import FontManager

from constants import *

class MainMenu(Gamable):
    def __init__(self) -> None:
        super().__init__()
        self.option_index = 0
        self.font = FontManager.get_font()
        self.options = [
            self.font.render('はじめ', True, (255, 255, 255)),
            self.font.render('設定', True, (255, 255, 255)),
            self.font.render('終了', True, (255, 255, 255))
        ]

        self.frame = 0
        self.blink_frame = 30
        self.move_frame = 10
        self.update_frame = 6
        self.apper = True
        

        self.snake = [
            # [BLOCK*12, BLOCK], [BLOCK*11, BLOCK], [BLOCK*10, BLOCK],
            # [BLOCK*9, BLOCK], [BLOCK*8, BLOCK], [BLOCK*7, BLOCK],
            # [BLOCK*6, BLOCK], [BLOCK*5, BLOCK], [BLOCK*4, BLOCK],
            [BLOCK*3, BLOCK], [BLOCK*2, BLOCK], [BLOCK*1, BLOCK]
        ]

    def update(self, change_game_state) -> None:
        self.input_master.poll_keyup()
        if self.input_master.direction == InputState.UP:
            self.option_index -= 1
        elif self.input_master.direction == InputState.DOWN:
            self.option_index += 1
        elif self.input_master.direction == InputState.ENTER:
            if self.option_index == 0:
                change_game_state(GameState.Running)
            elif self.option_index == 1:
                change_game_state(GameState.SettingsMenu)
            elif self.option_index == 2:
                change_game_state(GameState.Exited)
        self.input_master.reset()

        if self.option_index >= len(self.options):
            self.option_index = 0
        if self.option_index < 0:
            self.option_index = len(self.options)-1

        if self.snake[0][0] >= WIDTH*BLOCK:
            self.snake[0][0] = 0
        if self.snake[0][1] >= HEIGHT*BLOCK+MENU_HEIGHT*BLOCK:
            self.snake[0][1] = 0

        if self.frame >= self.update_frame:
            oldX = self.snake[0][0]
            oldY = self.snake[0][1]
            self.snake[0][0] += BLOCK
            if random.randint(0, 3) == 1:
                self.snake[0][1] += BLOCK
            for piece in self.snake[1:]:
                tempOldX = piece[0]
                tempOldY = piece[1]
                piece[0] = oldX
                piece[1] = oldY
                oldX = tempOldX
                oldY = tempOldY
            self.frame = 0
        
        self.frame += 1

        return 'Menu'

    def draw(self, surface):
        for index, piece in enumerate(self.snake):
            if(index == 0):
                pygame.draw.rect(surface, (0, 255, 0), (piece[0], piece[1], BLOCK, BLOCK ), 1, 5)
            else:
                pygame.draw.rect(surface, (255, 255, 255), (piece[0], piece[1], BLOCK, BLOCK ), 1, 5)

        mid_x = BLOCK*WIDTH/2
        mid_y = BLOCK*HEIGHT/2;
        for index, option in enumerate(self.options):
            y = mid_y+index*BLOCK*2
            if index == self.option_index:
                surface.blit(self.font.render('.(☞ﾟヮﾟ)☞', True, (255, 255, 255)), (mid_x-120, y))
            surface.blit(option, (mid_x, y))



        title_font = FontManager.get_font(font_size=48)
        title = title_font.render('蛇食字', True, (255, 255, 255))
        title_x = (WIDTH*BLOCK-title.get_width()) / 2
        surface.blit(title, (title_x, HEIGHT/8*BLOCK))



