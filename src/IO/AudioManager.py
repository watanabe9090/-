import pygame, os, sys

pygame.init()

class AudioManager:
    _current_music = pygame.mixer.Sound("/home/raijin/Development/Python/hebikuji/src/assets/audio.mp3")
    _stoped = True
    _paused = False

    @staticmethod
    def change_music():
        pygame.mixer.music.fadeout(500)

    @staticmethod
    def load():
        pygame.mixer.music.load("/home/raijin/Development/Python/hebikuji/src/assets/audio.mp3")

    @staticmethod
    def stop():
        pygame.mixer.music.stop()

    @staticmethod
    def pause():
        pygame.mixer.music.pause()
    
    @staticmethod
    def unpause():
        pygame.mixer.music.unpause()
    
    @staticmethod
    def play():
        pygame.mixer.Sound.play()
    
    @staticmethod
    def set_volume():
        pass

    def get_volume():
        pass

    def inc_volume():
        pass

    def dec_volume():
        pass

AudioManager.load()
AudioManager.play()

gameDisplay = pygame.display.set_mode((200, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("UNPAUSE")
                AudioManager.unpause()
            if event.key == pygame.K_p:
                print("PAUSE")
                AudioManager.pause()
