import pygame

import img_loader as img

class entity:
    def __init__(self) -> None:
        self.pos = [] # dynamic position

    def set_new_position(self, pos:tuple):
        self.pos = [pos[0], pos[1]]

    def update_pos(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

class copper(entity):
    def __init__(self) -> None:
        super().__init__()

    def set_pos(self, new_pos:tuple):
        self.pos = new_pos

    def draw_shape(self, pos:tuple, surface:pygame.Surface):
        surface.blit(img.copper, pos)

        

