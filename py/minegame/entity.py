import pygame
import os

import transport

class entity:
    def __init__(self) -> None:
        self.pos = [] # dynamic position
        self.size = (12, 12)

    def set_new_position(self, pos:tuple):
        self.pos = [pos[0], pos[1]]

    def update_pos(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

class copper(entity):
    def __init__(self) -> None:
        super().__init__()
        self.index_on_conv = 0
        self.img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphics', 'ores', 'copper.png')).convert_alpha()

    def set_pos(self, new_pos:tuple):
        self.pos = new_pos

    def draw_shape(self, pos:tuple, surface:pygame.Surface):
        surface.blit(self.img, pos)

        

