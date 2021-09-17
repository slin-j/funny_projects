import pygame

class miner:
    def __init__(self, position:tuple) -> None:
        if len(position) == 2:
            self.position = position
            self.size = (20, 20) # px

    def draw_shape(self, surface:pygame.Surface):
        r = pygame.Rect(self.position, self.size)
        pygame.draw.rect(surface, [255, 0 , 255], r)
