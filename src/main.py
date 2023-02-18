import sys, pygame, random

from constants import *

from menus.MainMenu import MainMenu
from menus.SettingsMenu import SettingsMenu
from menus.GameOverMenu import GameOverMenu
from menus.AudioSettingsMenu import AudioSettingsMenu

from game_objects.Snake import Snake
from game_objects.Kanji import Kanji

from Game import Game

pygame.init()

resolution = (BLOCK*WIDTH+1, BLOCK*HEIGHT+1+MENU_HEIGHT*BLOCK)
clock = pygame.time.Clock()
font = pygame.font.SysFont('msgothic', 16)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('蛇食字')



snake = Snake()
frame = 0
maxFrame = 5
fruit = Kanji(64, 64)
isRunning = True
points = 0
gameState = 'Menu' #


menu = MainMenu()
menuSettings = SettingsMenu()
audioSettingsMenu = AudioSettingsMenu(0)
gameOver = GameOverMenu()

def changeGameState(state):
    global gameState
    
    if state == 'Game':
        global snake
        global frame
        global fruit
        global points
        snake = Snake()
        frame = 0
        fruit = Kanji(64, 64)
        points = 0
    gameState = state

while isRunning:
    if gameState == 'Menu':
        changeGameState(menu.update())
        screen.fill((0, 0, 0))
        menu.draw(screen)
        clock.tick(60)
        pygame.display.flip()
    elif gameState == 'Exited':
        sys.exit()
    elif gameState == 'Settings':
        changeGameState(menuSettings.update())
        screen.fill((0, 0, 0))
        menuSettings.draw(screen)
        clock.tick(60)
        pygame.display.flip()
    elif gameState == 'AudioSettings':
        changeGameState(audioSettingsMenu.update())
        screen.fill((0, 0, 0))
        audioSettingsMenu.draw(screen)
        clock.tick(60)
        pygame.display.flip()
    elif gameState == 'GameOver':
        gameState = gameOver.update()
        screen.fill((0, 0, 0))
        gameOver.draw(screen)
        clock.tick(60)
        pygame.display.flip()

    elif gameState == 'Game':
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w] and snake.direction != 'DOWN'):
            snake.direction = 'UP'
        elif(keys[pygame.K_s] and snake.direction != 'UP'):
            snake.direction = 'DOWN'
        elif(keys[pygame.K_a] and snake.direction != 'RIGHT'):
            snake.direction = 'LEFT'
        elif(keys[pygame.K_d] and snake.direction != 'LEFT'):
            snake.direction = 'RIGHT'

        if(frame >= maxFrame):
            
            snake.update()
            if snake.x >= WIDTH*BLOCK or snake.x < 0 or snake.y >= HEIGHT*BLOCK or snake.y < 0:
                gameState = 'GameOver'
            if snake.isSelfColisioned():
                gameState = 'GameOver'
            if fruit.isColided(snake.x, snake.y):
                x = random.randint(0, WIDTH-1)
                y = random.randint(0, HEIGHT-1)
                fruit = Kanji(BLOCK*x, BLOCK*y)
                points += 10
                if len(snake.body) == 0:
                    snake.body.append([snake.x, snake.y])
                else:
                    snake.body.append([snake.body[-1][0], snake.body[-1][1]])

            screen.fill((0, 0, 0))
            snake.draw(screen)
            fruit.draw(screen)
            # Board
            for i in range(HEIGHT+1):
                pygame.draw.line(screen, (130, 128, 124), (0, i*BLOCK), (WIDTH*BLOCK, i*BLOCK), 1)
            for i in range(WIDTH+1):
                pygame.draw.line(screen, (130, 128, 124), (i*BLOCK, 0), (i*BLOCK, HEIGHT*BLOCK), 1)
            # Points
            screen.blit(font.render('点数:', True, (255, 255, 255)), (BLOCK*2,HEIGHT*BLOCK + MENU_HEIGHT*BLOCK*(2/3)))
            screen.blit(font.render(str(points), True, (255, 255, 255)), (BLOCK*6,HEIGHT*BLOCK + MENU_HEIGHT*BLOCK*(2/3)))
            frame = 0

        clock.tick(60)
        frame+=1
        pygame.display.flip()