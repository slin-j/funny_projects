import pygame 

class earth:
    def __init__(self, surface:pygame.display) -> None:
        self.bg = pygame.Surface(surface.get_size()).convert() # surface

    def draw_background(self):
        self.bg.fill([16,176,33])