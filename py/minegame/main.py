import sys
import pygame
import time

import environment
import resource_collect
import transport
import entity
import storage

SCR_WIDTH = 1000
SCR_HEIGHT = 600

pygame.init()

pygame.display.set_caption('minegame')
clock = pygame.time.Clock()
game_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen
# menu_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen

game_map = environment.earth(game_surface)
miner1 = resource_collect.miner((15*20,10*20))
cont1 = storage.storage_container((40*20,25*20))
#conv1 = transport.conveyor_belt([(16*20,10*20), (17*20,10*20), (18*20,10*20), (19*20,10*20), (20*20,10*20), (21*20,10*20), (22*20,10*20), (23*20,10*20), (24*20,10*20), (25*20,10*20), (25*20,11*20), (25*20,12*20), (25*20,13*20), (25*20,14*20), (26*20,14*20), (27*20,14*20), (28*20,14*20), (29*20,14*20), (30*20,14*20), (31*20,14*20)])

conveyor_list = []
conveyor_list.append(transport.conveyor_belt([(x*20,10*20) for x in range(16,40)] + 
                                             [(40*20,y*20) for y in range(10,25)]))

miner1.set_out_belt(conveyor_list[0])
cont1.set_in_belt(conveyor_list[0])

font_normal = pygame.font.SysFont("monospace",16)

i = 0

while True:
    clock.tick(100) # fps
    
    # user input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_f:
                conveyor_list[0].add_material(entity.copper())

    for c in conveyor_list:
        c.move_materials()

    miner1.update_spawner() 
    miner1.export_material_to_belt()

    cont1.import_material_from_belt()
    cont1.get_mat_from_input()

    print(len(cont1.storage))

    # draw plain map
    game_map.draw_dbg_grid(SCR_HEIGHT, SCR_WIDTH)
    # draw machines and belts on map
    miner1.draw_shape(game_map.bg)
    cont1.draw_shape(game_map.bg)
    for c in conveyor_list:
        c.draw_shape_with_materials(game_map.bg)
    
    # show new graphics
    game_surface.blit(game_map.bg, (0, 0))
    text = font_normal.render("Score {0}".format(69), 1, (0,0,0))
    game_surface.blit(text, (5,10))
    pygame.display.update()

    i += 1
    if i == 100: i = 0


#           /|        
#      /\ _/_|_ /\    
#      \.'     './    
#      | (o) (o) |    
#       .       .     
#       / `---´ \     
#     .'         '.   
#   .+-.\   |   /.-+. 
#  ( ## )\  |  /( ## )
#   '--'  ¯¯ˆ¯¯  '--'  
