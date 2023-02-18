import pygame, sys

class InputState:
    NONE, STOP, UP, DOWN, LEFT, RIGHT, ENTER = range(7)

class InputMaster:
    def __init__(self, direction=InputState.STOP) -> None:
        self.direction = direction
        self.joisticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

    # def joy_poll(self, event):

    def reset(self):
        self.direction = InputState.NONE


    def poll_keyup(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.direction = InputState.UP
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.direction = InputState.DOWN
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.direction = InputState.LEFT
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.direction = InputState.RIGHT
                if event.key == pygame.K_RETURN:
                    self.direction = InputState.ENTER

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                pass
            if event.type == pygame.JOYBUTTONUP:
                pass

        keys = pygame.key.get_pressed()
        if((keys[pygame.K_w] or keys[pygame.K_UP]) and self.direction != InputState.DOWN):
            self.direction = InputState.UP
        elif((keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.direction != InputState.UP):
            self.direction = InputState.DOWN
        elif((keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.direction != InputState.RIGHT):
            self.direction = InputState.LEFT
        elif((keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.direction != InputState.LEFT):
            self.direction = InputState.RIGHT

