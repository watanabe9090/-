from abc import ABC, abstractmethod
from IO.InputMaster import InputMaster

class Gamable(ABC):
    def __init__(self) -> None:
        self.input_master = InputMaster()

    @abstractmethod
    def update(self, change_game_state):
        pass

    @abstractmethod
    def draw(self, surface):
        pass