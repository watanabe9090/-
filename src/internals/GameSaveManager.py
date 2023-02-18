import os
import json


class GameSaveManager:
    def __init__(self) -> None:
        self.teste = 'teste'
    
    filepath = os.path.join(os.getcwd(), 'save.json')
    save_obj = {
        'level': 0,
        'name': '',
        'max_points': 0,
    }

    @staticmethod
    def load():
        with open(GameSaveManager.filepath, 'r') as f:
            save_obj = f.read()
            GameSaveManager.save_obj = json.loads(save_obj)

    @staticmethod
    def save():
        with open(GameSaveManager.filepath, 'w') as f:
            json_obj = json.dumps(GameSaveManager.save_obj.content)
            f.write(json_obj)

    def set(state: dict) -> None:
        GameSaveManager.save_obj = state 
