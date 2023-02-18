import pygame, sys, random
from kanjis_render import get_kanjis
from constants import *

from IO.FontManager import FontManager

class Kanji:
    last_font = FontManager.font_name
    kanjis = get_kanjis()

    def __init__(self, x: int = BLOCK*WIDTH/2, y: int = BLOCK*HEIGHT/2) -> None:
        self.x = x
        self.y = y
        if Kanji.last_font != FontManager.font_name:
            Kanji.last_font = FontManager.font_name
            Kanji.kanjis = get_kanjis()
        self.kanji = Kanji.kanjis[random.randint(0, len(Kanji.kanjis) - 1)]

    def draw(self, surface) -> None:
        print(str(self.x) + " : " + str(self.y) + "  -  H: " + str(self.kanji.get_height()) + "  -  W:"+str(self.kanji.get_width()))
        surface.blit(self.kanji, (self.x, self.y))
    
    def is_colided(self, x, y) -> bool:
        return self.x == x and self.y == y
       