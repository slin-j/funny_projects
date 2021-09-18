import pygame
import time

import transport

STORAGE_SIZE = 1000

class storage_container(transport.interface_in, transport.interface_out):
    def __init__(self, position:tuple) -> None:
        super().__init__()
        self.in_buffer_size = 1
        self.out_buffer_size = 1
        if len(position) == 2:
            self.pos = position
            self.storage = []
            self.size = (20, 20) # px

    def draw_shape(self, surface:pygame.Surface):
        r = pygame.Rect(self.pos, self.size)
        pygame.draw.rect(surface, [0, 0 , 0], r)

    # parent override to dodge in_buffer since its not needed for storage
    def export_material_to_belt(self):
        if len(self.storage) >= 1 and self.out_belt.is_first_piece_empty() == True:
            self.out_belt.add_material(self.storage.pop(0))
        return False

    # parent override to dodge out_buffer since its not needed for storage
    def import_material_from_belt(self):
        if len(self.storage) < STORAGE_SIZE:
            e = self.in_belt.collect_entity()
            if e != None: self.storage.append(e)
