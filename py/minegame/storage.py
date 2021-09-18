import pygame
import time

import transport

STORAGE_SIZE = 1000

class storage_container(transport.interface_in, transport.interface_out):
    def __init__(self, position:tuple) -> None:
        super().__init__()
        self.in_buffer_size = 1
        if len(position) == 2:
            self.pos = position
            self.storage = []
            self.size = (20, 20) # px

    def draw_shape(self, surface:pygame.Surface):
        r = pygame.Rect(self.pos, self.size)
        pygame.draw.rect(surface, [0, 0 , 0], r)

    def get_mat_from_input(self):
        if len(self.storage) < STORAGE_SIZE and len(self.in_buffer) > 0:
            self.storage.append(self.in_buffer.pop(0))
