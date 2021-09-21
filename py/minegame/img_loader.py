import pygame
import os

import transport

SCR_WIDTH = 1000
SCR_HEIGHT = 600

pygame.init()
s = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT),0,32)

no_texture = pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphics', 'texture_not_found.png')).convert_alpha()

belt = []
# BELT TIER 1 - 5
for i in range(5):
    belt.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphics', 'belts', f'tier{i+1}_straight.png')).convert_alpha())    # left to right
    belt.append(pygame.transform.rotate(belt[(i*8)], 90))   # down to up
    belt.append(pygame.transform.rotate(belt[(i*8)], 180))  # right to left
    belt.append(pygame.transform.rotate(belt[(i*8)], 270))  # up to down
    belt.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphics', 'belts', f'tier{i+1}_angled.png')).convert_alpha())     # left to up
    belt.append(pygame.transform.rotate(belt[(i*8) + 4], 90))   # down to left
    belt.append(pygame.transform.rotate(belt[(i*8) + 4], 180))  # right to down 
    belt.append(pygame.transform.rotate(belt[(i*8) + 4], 270))  # up to right 

# MATERIALS
copper = pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphics', 'ores', 'copper.png')).convert_alpha()

def calculate_beltpiece_img(input:list[transport.belt_piece], belt_tier:int) -> int:
        belt_tier -= 1
        # no connected block found
        if len(input[0].pos) != 2: # no input block found
            if input[1].pos[0] < input[2].pos[0]: # out to the right
                return int(0 + belt_tier*8)
            if input[1].pos[1] > input[2].pos[1]: # out to top
                return int(1 + belt_tier*8)
            if input[1].pos[0] > input[2].pos[0]: # out to the left
                return int(2 + belt_tier*8)
            if input[1].pos[1] < input[2].pos[1]: # out to bottom
                return int(3 + belt_tier*8)
        if len(input[2].pos) != 2: # no output block found
            if input[0].pos[0] > input[1].pos[0]: # in from the right
                return int(2 + belt_tier*8)
            if input[0].pos[1] < input[1].pos[1]: # in from top
                return int(3 + belt_tier*8)
            if input[0].pos[0] < input[1].pos[0]: # in from the left
                return int(0 + belt_tier*8)
            if input[0].pos[1] > input[1].pos[1]: # in from below
                return int(1 + belt_tier*8)
        # run belt in the connected block 
        if input[0].pos[0] < input[1].pos[0]: # in from the left
            if input[1].pos[0] < input[2].pos[0]: # out to the right
                return int(0 + belt_tier*8)
            if input[1].pos[1] > input[2].pos[1]: # out to top
                return int(4 + belt_tier*8)
            if input[1].pos[1] < input[2].pos[1]: # out to bottom
                return int(5 + belt_tier*8)
        if input[0].pos[0] > input[1].pos[0]: # in from the right
            if input[1].pos[0] > input[2].pos[0]: # out to the left
                return int(2 + belt_tier*8)
            if input[1].pos[1] < input[2].pos[1]: # out to bottom
                return int(6 + belt_tier*8)
            if input[1].pos[1] > input[2].pos[1]: # out to top
                return int(7 + belt_tier*8)
        if input[0].pos[1] > input[1].pos[1]: # in from below
            if input[1].pos[1] > input[2].pos[1]: # out to top
                return int(1 + belt_tier*8)
            if input[1].pos[0] > input[2].pos[0]: # out to the left
                return int(5 + belt_tier*8)
            if input[1].pos[0] < input[2].pos[0]: # out to the right
                return int(6 + belt_tier*8)
        if input[0].pos[1] < input[1].pos[1]: # in from top
            if input[1].pos[1] < input[2].pos[1]: # out to bottom
                return int(3 + belt_tier*8)
            if input[1].pos[0] < input[2].pos[0]: # out to the right
                return int(7 + belt_tier*8)
            if input[1].pos[0] > input[2].pos[0]: # out to the left
                return int(4 + belt_tier*8)

        return -1 # no texture