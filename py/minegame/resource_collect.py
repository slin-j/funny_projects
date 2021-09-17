import pygame
import time

class miner:
    def __init__(self, position:tuple) -> None:
        self.PRODUCTION_RATE = 600e6 # 400ms
        self.last_update = time.time_ns()

        if len(position) == 2:
            self.position = position
            self.size = (20, 20) # px

    def draw_shape(self, surface:pygame.Surface):
        r = pygame.Rect(self.position, self.size)
        pygame.draw.rect(surface, [255, 0 , 255], r)

    def did_material_spawn(self) -> bool:
        if time.time_ns() - self.last_update >= self.PRODUCTION_RATE:
            self.last_update += self.PRODUCTION_RATE
            return True #todo return a string for ex with materialtype that can be interpreted and changed to a obj
        
        return False
