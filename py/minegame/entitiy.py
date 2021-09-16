import pygame

import transport

class entitiy:
    def __init__(self) -> None:
        self.pos = [] # dynamic position
        self.size = (12, 12)

    def set_new_position(self, pos:tuple):
        self.pos = [pos[0], pos[1]]

    def update_pos(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

class copper(entitiy):
    def __init__(self, conv_to_follow:list) -> None:
        super().__init__()
        self.path = conv_to_follow
        self.pos = conv_to_follow[0]

    def draw_shape(self, surface:pygame.Surface):
        r = pygame.Rect((self.pos[0]+4, self.pos[1]+4), self.size)
        pygame.draw.rect(surface, [150, 67, 8], r)

    def update_pos_on_conveyor(self) -> bool:
        if len(self.path) <= 0:
            return False
        self.pos = self.path[0]
        self.path.pop(0)
        return True
        

