import pygame
import sys
import random

# ===CLASSES====================================================================
class snake():
    def __init__(self):
        self.length = 1
        self.score = 0
        self.postitions = [(0,0)]
        self.direction = random.choice([RIGHT])
        self.Color = (255,0,255)

    def get_head_pos(self):
        return self.postitions[0]

    def turn(self,move_direction):
        # set direction
        if self.length > 1 and (move_direction[0]*-1, move_direction[1]*-1) == self.direction:
            return
        else:
            self.direction = move_direction

    def move(self):
        # move
        current_head = self.get_head_pos()
        x,y = self.direction
        new_head_pos = (((current_head[0] + (x*GRID_SQARE_WIDTH))%SCR_WIDTH), (current_head[1] + (y*GRID_SQARE_HEIGHT))%SCR_HEIGHT)
        if len(self.postitions) > 2 and new_head_pos in self.postitions[2:]:
            self.reset()
        else:
            self.postitions.insert(0,new_head_pos)
            if len(self.postitions) > self.length:
                self.postitions.pop()

        if snake.get_head_pos() == food.position:
            snake.length += 1
            snake.score += 1
            food.set_new_position()

    def reset(self):
        self.length = 1
        self.score = 0
        self.postitions = [(SCR_WIDTH / 2, SCR_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw_body(self,bg):
        for pos in self.postitions:
            rect = pygame.Rect((pos[0],pos[1]),(GRID_SQARE_WIDTH,GRID_SQARE_HEIGHT)) # (position),(dimension)
            pygame.draw.rect(bg,self.Color,rect)

    def handle_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            """elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)"""

class food():
    def __init__(self):
        self.Color = (255,64,0)
        self.position = (0,0)
        self.set_new_position()

    def set_new_position(self):
        self.position = (random.randint(0,(GRID_SQARE_CNT-1))*GRID_SQARE_WIDTH,
                         random.randint(0,(GRID_SQARE_CNT-1))*GRID_SQARE_HEIGHT)

    def draw(self,bg):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SQARE_WIDTH, GRID_SQARE_HEIGHT)) # (position),(dimension)
        pygame.draw.rect(bg,self.Color,rect)

# ===DEFINES====================================================================
SCR_WIDTH = 480
SCR_HEIGHT = 480
GRID_SQARE_CNT = 20
GRID_SQARE_WIDTH = SCR_WIDTH / GRID_SQARE_CNT       # 480 / 20 = 24
GRID_SQARE_HEIGHT = SCR_HEIGHT / GRID_SQARE_CNT

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

# ===FUNCTIONS==================================================================
def drawGrid(bg):
    for y in range(0,int(GRID_SQARE_CNT)):
        for x in range(0,int(GRID_SQARE_CNT)):
            if (x + y) % 2:
                rect = pygame.Rect((GRID_SQARE_WIDTH*x,GRID_SQARE_HEIGHT*y),(GRID_SQARE_WIDTH,GRID_SQARE_HEIGHT))   # (position),(dimension)
                pygame.draw.rect(bg,(152, 230, 66),rect)
            else:
                rect = pygame.Rect((GRID_SQARE_WIDTH*x,GRID_SQARE_HEIGHT*y),(GRID_SQARE_WIDTH,GRID_SQARE_HEIGHT))   # (position),(dimension)
                pygame.draw.rect(bg,(93, 230, 66),rect)


# ===MAIN=======================================================================
pygame.init()

pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen

background = pygame.Surface(window_surface.get_size()) # surface
background = background.convert()
drawGrid(background)

snake = snake()
food = food()

myfont = pygame.font.SysFont("monospace",16)

is_running = True
while True:
    clock.tick(10000)

    p = snake.get_head_pos()

    if p[0] == (SCR_WIDTH - GRID_SQARE_WIDTH):       # head at the right side of screen
        snake.turn(DOWN)
        snake.move()
        snake.turn(LEFT)
        snake.move()
    elif p[0] == (GRID_SQARE_WIDTH) and p[1] != 0 and p[1] != (SCR_HEIGHT - GRID_SQARE_HEIGHT):
        snake.turn(DOWN)
        snake.move()
        snake.turn(RIGHT)
        snake.move()
    elif p[0] == 0 and p[1] == 0:
        snake.turn(RIGHT)
        snake.move()
    elif p[0] == (GRID_SQARE_WIDTH) and p[1] == (SCR_HEIGHT - GRID_SQARE_HEIGHT):
        snake.turn(LEFT)
        snake.move()
        snake.turn(UP)
        snake.move()

    snake.handle_user_input()
    drawGrid(background)    # redraw grid -> snake/food must be redrawn too
    snake.move()

    food.draw(background)
    snake.draw_body(background)

    window_surface.blit(background, (0, 0))
    text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
    window_surface.blit(text, (5,10))
    pygame.display.update()
