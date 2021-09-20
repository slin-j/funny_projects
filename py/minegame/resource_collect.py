import pygame
import time
import numpy as np

import entity
import transport

class miner(transport.interface_out):
    def __init__(self, position:tuple) -> None:
        super().__init__()
        self.PRODUCTION_RATE = 2.222e8 # 400ms
        self.last_update = time.time_ns()

        if len(position) == 2:
            self.position = position
            self.size = (20, 20)

    def draw_shape(self, surface:pygame.Surface):
        r = pygame.Rect(self.position, self.size)
        pygame.draw.rect(surface, [255, 0 , 255], r)

    # update internalbuffer with newly spawned material and return the length of the buffer
    def update_spawner(self):
        if time.time_ns() - self.last_update >= self.PRODUCTION_RATE:
            self.last_update += self.PRODUCTION_RATE
            if len(self.out_buffer) < 100 and len(self.out_buffer) >= 0:
                self.out_buffer.append(entity.copper()) #todo settable materialtype

