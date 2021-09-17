import pygame
import time

import entitiy

class conveyor_belt: 
    def __init__(self, positions:list[tuple]) -> None:
        self.UPDATE_INTERVAL = 200e6 # 200ms
        self.last_update = time.time_ns()

        self.positions = positions
        self.size = (20, 20) # px
        self.materials = [] # list with all entity-obj that are on this belt

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
        if time.time_ns() - self.last_update >= self.UPDATE_INTERVAL:
            self.last_update += self.UPDATE_INTERVAL
            # print(len(self.materials))
            r = 0
            for i in range(len(self.materials)):
                self.materials[i-r].index_on_conv += 1
                if self.materials[i-r].index_on_conv > (len(self.positions) - 1):
                    self.materials.remove(self.materials[i-r])
                    r += 1
            #todo what to do when belt ends?

    def get_positions(self) -> list[tuple]:
        return self.positions.copy()

    def extend(self, new_positions:list[tuple]):
        self.positions.extend(new_positions)