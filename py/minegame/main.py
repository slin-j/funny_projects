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
import player

def get_grid_cursor_pos():
    return (math.floor(pygame.mouse.get_pos()[0]/20)*20, math.floor(pygame.mouse.get_pos()[1]/20)*20)

pygame.init()

pygame.display.set_caption('minegame')
clock = pygame.time.Clock()
game_surface = pygame.display.set_mode((img_loader.SCR_WIDTH, img_loader.SCR_HEIGHT),0,32)  # screen
btn_manager = pygame_gui.UIManager((img_loader.SCR_WIDTH,img_loader.SCR_HEIGHT))
# menu_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen

user = player.minegame_gamer()

# gui elements
btn1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (20, 20)), text='t1', manager=btn_manager)

game_map = environment.earth(game_surface)
user.miner_list.append(resource_collect.miner((15*20,10*20)))
user.storage_list.append(storage.storage_container((40*20,25*20)))

user.conveyor_list.append(transport.conveyor_belt(([(x*20,10*20) for x in range(16,40)] + [(40*20,y*20) for y in range(10,25)]), tier=3))
user.conveyor_list.append(transport.conveyor_belt(([x*20, 26*20] for x in range(40,20,-1)), tier=3))

user.miner_list[0].set_out_belt(user.conveyor_list[0], user.miner_list[0].pos)
user.storage_list[0].set_in_belt(user.conveyor_list[0], user.storage_list[0].pos)
user.storage_list[0].set_out_belt(user.conveyor_list[1], user.storage_list[0].pos)

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
                user.conveyor_list[0].add_material(entity.copper())

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
                if event.button == 1: # LMB
                    if transport.validate_belt_geometry(build_list) == True:
                        user.conveyor_list.append(transport.conveyor_belt(build_list, tier=3))
                    else:
                        print('invalid belt-shape!') #todo change to a ui warning
                    build_list = []
                
        btn_manager.process_events(event)
    btn_manager.update(dt)

    for c in user.conveyor_list:
        c.move_materials()

    user.update_inout_interfaces()

    # print(len(cont1.storage))

    # draw plain map
    game_map.draw_dbg_grid(img_loader.SCR_HEIGHT, img_loader.SCR_WIDTH)
    # draw machines and belts on map
    user.draw_machine_shapes(game_map.bg)
    
    # show all belt-graphics
    for j in range(5):
        for i in range(8):
            game_map.bg.blit(img_loader.belt[i + (j*8)], (20 + (i*20),40 + (j*20)))
    
    # show new graphics
    game_surface.blit(game_map.bg, (0, 0))
    text = font_normal.render(f"coord {get_grid_cursor_pos()}", 1, (0,0,0))
    game_surface.blit(text, (5,10))
    btn_manager.draw_ui(game_surface)

    # user mouse-pos in grid (rounded down to the next %20 == 0)
    s = pygame.Surface((20,20))
    s.set_alpha(64)
    s.fill([0,0,0])
    game_surface.blit(s, get_grid_cursor_pos())

    # draw path when drawing belts
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
