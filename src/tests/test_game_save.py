# import unittest

from internals.GameSaveManager import GameSaveManager

# class TestGameSave(unittest.TestCase):
#     def test_save(self):
#         self.assertEqual()



# if __name__ == '__name__':
#     unittest.main()

def test_a():
    save = {
        'level': 10,
        'name': 'TESTER_A',
        'max_points': 150
    }
    GameSaveManager.set(save)
    assert GameSaveManager.save_obj['level'] == save['level']
    assert GameSaveManager.save_obj['name'] == save['level']
    assert GameSaveManager.save_obj['max_points'] == save['level']
    # GameSaveManager.save(save)