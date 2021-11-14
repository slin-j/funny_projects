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
# menu_surface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)  # screen
build_menu = environment.build_menu(game_surface)

user = player.minegame_gamer()

game_map = environment.earth(game_surface)
user.miner_list.append(resource_collect.miner((15*20,10*20)))
user.miner_list.append(resource_collect.miner((20,300)))
user.storage_list.append(storage.storage_container((40*20,25*20)))
user.storage_list.append(storage.storage_container((200,300)))

user.conveyor_list.append(transport.conveyor_belt(([(x*20,10*20) for x in range(16,40)] + [(40*20,y*20) for y in range(10,25)]), tier=5))
user.conveyor_list.append(transport.conveyor_belt(([x*20, 26*20] for x in range(40,20,-1)), tier=3))

user.miner_list[0].set_out_belt(user.conveyor_list[0], user.miner_list[0].pos)
user.storage_list[0].set_in_belt(user.conveyor_list[0], user.storage_list[0].pos)
user.storage_list[0].set_out_belt(user.conveyor_list[1], user.storage_list[0].pos)

font_normal = pygame.font.SysFont("monospace",16)

is_build_mode = False
is_build_menu = False
build_list = []

while True:
    dt = clock.tick(144)/1000.0 # fps
    
    # user input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: #! just for development
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_ESCAPE:
                is_build_mode = False
                is_build_menu = False
                build_menu.set_visibility(False)
            if event.key == pygame.K_b:
                build_menu.set_visibility(not build_menu.visible)

        # if event.type == pygame.USEREVENT:
        #     if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        #         is_build_mode = build_menu.handle_btn_pressed(event.ui_element)
        #         print(is_build_mode)
        
        if is_build_mode != False:
            # print(is_build_mode)
            if pygame.mouse.get_pressed()[0]:
                p = get_grid_cursor_pos()
                if p not in build_list:
                    build_list.append(p)
                if transport.validate_belt_geometry(user, build_list) == False and len(build_list) > 1:
                    build_list.remove(p)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # LMB
                    if transport.validate_belt_geometry(user, build_list) == True:
                        #! belt must strart/end on the same positions as the machines
                        # check if any machines are found to bind belt to 
                        pin, pout = False, False
                        if user.is_pos_occupied(build_list[0]) != False: pin = build_list.pop(0)
                        if user.is_pos_occupied(build_list[-1]) != False: pout = build_list.pop(-1)
                        user.conveyor_list.append(transport.conveyor_belt(build_list, tier=5)) # create belt

                        if pin != False: user.bind_belt_to_machine(user.conveyor_list[-1], False, pin)
                        if pout != False: user.bind_belt_to_machine(user.conveyor_list[-1], True, pout)       
                    else:
                        print('invalid belt-shape!') #todo change to a ui warning
                    build_list = []

    build_mode = build_menu.handle_btn_pressed(dt)
        

    for c in user.conveyor_list:
        c.move_materials()

    user.update_inout_interfaces()

    # print(len(user.storage_list[0].storage))
    # print(len(user.miner_list[-1].out_buffer))

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
    build_menu.draw_prompt(game_surface)

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
