import pygame, sys

from constants import *
from IO.InputMaster import InputState

class Snake:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.direction = InputState.STOP
        self.body = []

    def update(self) -> None:
        oldY = self.y
        oldX = self.x
        if self.direction == InputState.UP:
            self.y -= BLOCK
        elif self.direction == InputState.DOWN:
            self.y += BLOCK
        elif self.direction == InputState.LEFT:
            self.x -= BLOCK
        elif self.direction == InputState.RIGHT:
            self.x += BLOCK

        for el in self.body:
            tempOldX = el[0]
            tempOldY = el[1]
            el[0] = oldX
            el[1] = oldY
            oldX = tempOldX
            oldY = tempOldY
    
    def move(self): 
        pass

    def is_self_colisioned(self) -> bool:
        for el in self.body:
            if el[0] == self.x and el[1] == self.y:
                return True
        return False

    def add_piece(self) -> None:
        if len(self.body) == 0:
            self.body.append([self.x, self.y])
        else:
            self.body.append([self.body[-1][0], self.body[-1][1]])

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, (150, 252, 48), pygame.Rect(self.x, self.y, BLOCK, BLOCK), 2, 7)
        for el in self.body:
            pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(el[0], el[1], BLOCK, BLOCK), 2, 7)