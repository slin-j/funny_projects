import sys, os
import pygame
import pygame_gui
import time
# === CLASSES ===
from board import board as chessBoard
#===========================DEFINES==========================================
SCR_WIDTH = 750
SCR_HEIGHT = 750
START_X = 10
START_Y = 75
FIELD_DIMENSION = 75

pygame.init()

pygame.display.set_caption('Chess')
clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen

background = pygame.Surface(window_surface.get_size()) # surface
background = background.convert()

chessBoard = chessBoard()
chessBoard.drawGrid(background, START_X, START_Y, FIELD_DIMENSION)

os.chdir(os.path.abspath('chess'))
os.chdir(os.path.abspath('figure_pics'))
img_bb = pygame.transform.scale(pygame.image.load('bb.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_bk = pygame.transform.scale(pygame.image.load('bk.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_bn = pygame.transform.scale(pygame.image.load('bn.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_bp = pygame.transform.scale(pygame.image.load('bp.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_bq = pygame.transform.scale(pygame.image.load('bq.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_br = pygame.transform.scale(pygame.image.load('br.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_wb = pygame.transform.scale(pygame.image.load('wb.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_wk = pygame.transform.scale(pygame.image.load('wk.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_wn = pygame.transform.scale(pygame.image.load('wn.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_wp = pygame.transform.scale(pygame.image.load('wp.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_wq = pygame.transform.scale(pygame.image.load('wq.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))
img_wr = pygame.transform.scale(pygame.image.load('wr.png').convert_alpha(), (FIELD_DIMENSION,FIELD_DIMENSION))




myfont = pygame.font.SysFont("monospace",16)

is_running = True
while True:
    clock.tick(10)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    window_surface.blit(background, (0, 0))
    window_surface.blit(img_bk, [START_X, START_Y])
    window_surface.blit(img_wk, [START_X+75, START_Y])

    pygame.display.update()
