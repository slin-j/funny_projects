import sys
import pygame

import environment
import test

pygame.init()

SCR_WIDTH = 1000
SCR_HEIGHT = 600

pygame.init()

pygame.display.set_caption('minegame')
clock = pygame.time.Clock()
game_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen
# menu_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen

game_map = environment.earth(game_surface)
miner1 = test.miner((5,5))

font_normal = pygame.font.SysFont("monospace",16)

while True:
    clock.tick(10) # gametick

    # user input events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    game_map.draw_background()
    miner1.draw_shape(game_map.bg)

    # show new graphics
    game_surface.blit(game_map.bg, (0, 0))
    text = font_normal.render("Score {0}".format(69), 1, (0,0,0))
    game_surface.blit(text, (5,10))
    pygame.display.update()
