import pygame, sys

from Gamable import Gamable
from GameState import GameState
from constants import *
from IO.FontManager import FontManager
from IO.InputMaster import InputState

class FontSettingsMenu(Gamable):
    def __init__(self) -> None:
        super().__init__()
        self.option_index = 0

        self.font_name = FontManager.font_name
        self.font = FontManager.get_font()
        self.font_index = FontManager.avaliable_font_names.index(self.font_name)

        self.back_option = self.font.render('戻る', True, WHITE)



    def update(self, change_game_state):
        print(FontManager.font_name)
        print(FontManager.get_font())
        self.input_master.poll_keyup()
        if self.input_master.direction == InputState.UP:
            pass
        if self.input_master.direction == InputState.DOWN:
            pass
        if self.input_master.direction == InputState.LEFT:
            self.font_index -=1
        if self.input_master.direction == InputState.RIGHT:
            self.font_index +=1
        if self.input_master.direction == InputState.ENTER:
            change_game_state(GameState.SettingsMenu)

        self.input_master.reset()

        if self.font_index < 0:
            self.font_index = len(FontManager.avaliable_font_names)-1
        elif self.font_index >= len(FontManager.avaliable_font_names):
            self.font_index = 0

        self.font_name = FontManager.avaliable_font_names[self.font_index]
        FontManager.font_name = self.font_name
        self.font = FontManager.get_font()

    def draw(self, surface):
        self.back_option = self.font.render('戻る', True, WHITE)
        x = (WIDTH*BLOCK - self.back_option.get_width()) / 2
        y = (HEIGHT*BLOCK - self.back_option.get_height()) / 2

        font_text = self.font.render(self.font_name, True, WHITE)
        font_x = (WIDTH*BLOCK - font_text.get_width()) / 2
        font_y = (HEIGHT*BLOCK - font_text.get_height()) / 2
        # surface.blit(self.font.render(CURSOR, True, WHITE), (mid_x-120, y))
        
        if self.option_index == 0:
            pass
        elif self.option_index == 1:
            pass
        surface.blit(font_text, (font_x, font_y))
        # surface.blit(self.back_option, (x, y))

