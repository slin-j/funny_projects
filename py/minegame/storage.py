import pygame

STORAGE_SIZE = 1000

class storage_container:
    def __init__(self, position:tuple) -> None:
        if len(position) == 2:
            self.pos = position
            self.storage = []
            self.input_belt = None
            self.output_belt = None
            self.size = (20, 20) # px

    def draw_shape(self, surface:pygame.Surface):
        r = pygame.Rect(self.pos, self.size)
        pygame.draw.rect(surface, [0, 0 , 0], r)

    def set_input_belt(self, b):
        self.input_belt = b

    def set_output_belt(self, b):
        self.output_belt = b

    def get_mat_from_input(self):
        if len(self.storage) < STORAGE_SIZE:
            e = self.input_belt.collect_entity()
            if e != None:
                self.storage.append(e)
