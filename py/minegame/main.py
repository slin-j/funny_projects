import sys
import pygame
import pygame_gui
import math
import time
import os

import environment
import resource_collect
import transport
import entity
import storage
import img_loader

def get_grid_cursor_pos():
    return (math.floor(pygame.mouse.get_pos()[0]/20)*20, math.floor(pygame.mouse.get_pos()[1]/20)*20)

pygame.init()

pygame.display.set_caption('minegame')
clock = pygame.time.Clock()
game_surface = pygame.display.set_mode((img_loader.SCR_WIDTH, img_loader.SCR_HEIGHT),0,32)  # screen
btn_manager = pygame_gui.UIManager((img_loader.SCR_WIDTH,img_loader.SCR_HEIGHT))
# menu_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen

# gui elements
btn1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (20, 20)), text='t1', manager=btn_manager)

game_map = environment.earth(game_surface)
miner1 = resource_collect.miner((15*20,10*20))
cont1 = storage.storage_container((40*20,25*20))
#conv1 = transport.conveyor_belt([(16*20,10*20), (17*20,10*20), (18*20,10*20), (19*20,10*20), (20*20,10*20), (21*20,10*20), (22*20,10*20), (23*20,10*20), (24*20,10*20), (25*20,10*20), (25*20,11*20), (25*20,12*20), (25*20,13*20), (25*20,14*20), (26*20,14*20), (27*20,14*20), (28*20,14*20), (29*20,14*20), (30*20,14*20), (31*20,14*20)])

conveyor_list = []
conveyor_list.append(transport.conveyor_belt(([(x*20,10*20) for x in range(16,40)] + 
                                             [(40*20,y*20) for y in range(10,25)]), tier=3))
conveyor_list.append(transport.conveyor_belt(([x*20, 26*20] for x in range(40,20,-1)), tier=3))

miner1.set_out_belt(conveyor_list[0], miner1.pos)
cont1.set_in_belt(conveyor_list[0], cont1.pos)
cont1.set_out_belt(conveyor_list[1], cont1.pos)

font_normal = pygame.font.SysFont("monospace",16)

is_build_mode = False
build_list = []

while True:
    dt = clock.tick(144)/1000.0 # fps
    
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

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == btn1:
                    is_build_mode = 'belt_tier1'
                    build_list = []
        
        if is_build_mode != False:
            # print(is_build_mode)
            if pygame.mouse.get_pressed()[0]:
                p = get_grid_cursor_pos()
                if p not in build_list:
                    build_list.append(p)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    conveyor_list.append(transport.conveyor_belt(build_list, tier=3))
                    build_list = []
                
        btn_manager.process_events(event)
    btn_manager.update(dt)

    for c in conveyor_list:
        c.move_materials()

    cont1.import_material_from_belt()
    cont1.export_material_to_belt()

    miner1.update_spawner() 
    miner1.export_material_to_belt()

    # print(len(cont1.storage))

    # draw plain map
    game_map.draw_dbg_grid(img_loader.SCR_HEIGHT, img_loader.SCR_WIDTH)
    # draw machines and belts on map
    miner1.draw_shape(game_map.bg)
    cont1.draw_shape(game_map.bg)
    for c in conveyor_list:
        c.draw_shape_with_materials(game_map.bg)
    
    # show all belt-graphics
    for j in range(5):
        for i in range(8):
            game_map.bg.blit(img_loader.belt[i + (j*8)], (20 + (i*20),40 + (j*20)))
    
    # show new graphics
    game_surface.blit(game_map.bg, (0, 0))
    text = font_normal.render(f"coord {get_grid_cursor_pos()}", 1, (0,0,0))
    game_surface.blit(text, (5,10))
    btn_manager.draw_ui(game_surface)

    s = pygame.Surface((20,20))
    s.set_alpha(64)
    s.fill([0,0,0])
    game_surface.blit(s, get_grid_cursor_pos())

    for b in build_list:
        s = pygame.Surface((20,20))
        s.set_alpha(192)
        s.fill([255,255,255])
        game_surface.blit(s, b)

    pygame.display.update()



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
