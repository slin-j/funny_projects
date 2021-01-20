import sys, os
import pygame
import pygame_gui
import time
# === CLASSES ===
from board import board as chessBoard
#===========================DEFINES==========================================
SCR_WIDTH = 800
SCR_HEIGHT = 900
START_X = 10
START_Y = 100
FIELD_DIMENSION = 100

pygame.init()

pygame.display.set_caption('Chess')
clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen

background = pygame.Surface(window_surface.get_size()) # surface
background = background.convert()

chessBoard = chessBoard()
chessBoard.drawGrid(background, START_X, START_Y, FIELD_DIMENSION)

image = pygame.image.load(os.path.join(sys.path[0], 'figure_pics/wk.png'))

myfont = pygame.font.SysFont("monospace",16)

is_running = True
while True:
    clock.tick(10)

    window_surface.fill((255,255,0))
    window_surface.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    window_surface.blit(background, (0, 0))
    pygame.display.update()
