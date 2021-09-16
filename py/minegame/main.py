import sys
import pygame

import environment
import resource_collect
import transport
import entitiy

SCR_WIDTH = 1000
SCR_HEIGHT = 600

pygame.init()

pygame.display.set_caption('minegame')
clock = pygame.time.Clock()
game_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen
# menu_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen

game_map = environment.earth(game_surface)
miner1 = resource_collect.miner((15*20,10*20))
conv = transport.conveyor_belt([(16*20,10*20), (17*20,10*20), (18*20,10*20), (19*20,10*20), (20*20,10*20), 
                                (21*20,10*20), (22*20,10*20), (23*20,10*20), (24*20,10*20), (25*20,10*20), 
                                (25*20,11*20), (25*20,12*20), (25*20,13*20), (25*20,14*20)])
copper = entitiy.copper(conv.get_positions())

entitiy_list = []
entitiy_list.append(copper)

font_normal = pygame.font.SysFont("monospace",16)

i = 0

while True:
    clock.tick(20) # gametick

    # user input events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    game_map.draw_background()
    miner1.draw_shape(game_map.bg)
    conv.draw_shape(game_map.bg)
    for e in entitiy_list: e.draw_shape(game_map.bg)
    i += 1
    if i == 5:
        i = 0
        for e in entitiy_list:
            if e.update_pos_on_conveyor() == False: del e; continue

    # show new graphics
    game_surface.blit(game_map.bg, (0, 0))
    text = font_normal.render("Score {0}".format(69), 1, (0,0,0))
    game_surface.blit(text, (5,10))
    pygame.display.update()
