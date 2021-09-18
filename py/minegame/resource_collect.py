import pygame
import time
import numpy as np

import entity

class miner:
    def __init__(self, position:tuple) -> None:
        self.PRODUCTION_RATE = 600e6 # 400ms
        self.last_update = time.time_ns()

        if len(position) == 2:
            self.position = position
            self.internal_buffer = []
            self.size = (20, 20) # px

    def draw_shape(self, surface:pygame.Surface):
        r = pygame.Rect(self.position, self.size)
        pygame.draw.rect(surface, [255, 0 , 255], r)

    # update internalbuffer with newly spawned material and return the length of the buffer
    def update_spawner(self):
        if time.time_ns() - self.last_update >= self.PRODUCTION_RATE:
            self.last_update += self.PRODUCTION_RATE
            if len(self.internal_buffer) < 100 and len(self.internal_buffer) >= 0:
                self.internal_buffer.append(entity.copper()) #todo settable materialtype
        return len(self.internal_buffer)

    def get_material_from_buffer(self, cnt:int):
        if len(self.internal_buffer) >= cnt and cnt < 100 and cnt > 0:
            r = self.internal_buffer[:cnt]
            self.internal_buffer = self.internal_buffer[cnt:]
            return r
        return False