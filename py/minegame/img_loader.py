import pygame
import os

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