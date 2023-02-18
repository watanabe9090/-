import sys, pygame, math

pygame.init()
BLOCK = 8
resolution = (BLOCK*100, BLOCK*80)
clock = pygame.time.Clock()
font = pygame.font.SysFont('msgothic', 16)
screen = pygame.display.set_mode(resolution)


map = [
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#',
    '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#',
    '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#',
    '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#',
    '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#',
    '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#',
    '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#',
    '#', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '#',
    '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
]

def delt_of(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

class Character:
    def __init__(self) -> None:
        self.x = 200
        self.y = 200
        self.angle = 0
        self.angle_vision = 50

char = Character()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_a] ):
        char.angle += 0.1
    elif(keys[pygame.K_d]):
        char.angle -= 0.1

    screen.fill((0, 0, 0))

    for index, block in enumerate(map):
        block_x = ( index % 10 ) * BLOCK
        block_y = ( index // 10 ) * BLOCK

        if block == '#':
            distance = delt_of(block_x, block_y, char.x, char.y)
            vision=(255-distance)
            if vision < 0: vision = 0
            color=(vision, vision, vision)


            x = block_x*BLOCK - char.x
            y = block_y*BLOCK - char.y
            pos_x = 0
            pos_y = 0
            if x < 0:
                pos_x = -x
            elif x >= 0:
                pos_x = x

            if y < 0:
                pos_y = -y
            elif y >= 0:
                pos_y = y
            
            screen.fill(color, (pos_x, pos_y, BLOCK, BLOCK))

        
    # pygame.draw.line(screen, (255, 255, 255), (char.x, char.y), (char.x-math.sin(char.angle)*50, char.y+math.cos(char.angle)*50))



    clock.tick(60)
    pygame.display.flip()