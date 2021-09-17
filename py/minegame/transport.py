import pygame
import time

import entitiy

class conveyor_belt: 
    def __init__(self, positions:list[tuple]) -> None:
        self.UPDATE_INTERVAL = 200e6 # 200ms
        self.positions = positions
        self.materials = []
        self.size = (20, 20) # px
        self.last_update = time.time_ns()

    def draw_shape_with_materials(self, surface:pygame.Surface):
        for p in self.positions:
            r = pygame.Rect(p, self.size)
            pygame.draw.rect(surface, [128, 128 , 128], r)
        for m in self.materials:
            m.draw_shape(self.positions[m.index_on_conv], surface)

    def add_material(self, new_mat:entitiy):
        self.materials.append(new_mat)
        # self.materials[-1].set_pos(self.positions[0]) # set startposition of new material to the beginning of the belt

    def incr_material_positions(self) -> bool:
        while time.time_ns() - self.last_update >= self.UPDATE_INTERVAL:
            self.last_update += self.UPDATE_INTERVAL
            for m in self.materials:
                m.index_on_conv += 1
                if m.index_on_conv > len(self.positions) - 1:
                    self.materials.remove(m)
            #todo what to do when conv ends?

    def get_positions(self) -> list[tuple]:
        return self.positions.copy()

    def extend(self, new_positions:list[tuple]):
        self.positions.extend(new_positions)