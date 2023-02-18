import pygame, sys, random
from kanjis_render import kanjis
from constants import *


class Kanji:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.kanji = kanjis[random.randint(0, len(kanjis) - 1)]

    def draw(self, surface) -> None:
        surface.blit(self.kanji, (self.x, self.y))
    
    def is_colided(self, x, y) -> bool:
        return self.x == x and self.y == y
       