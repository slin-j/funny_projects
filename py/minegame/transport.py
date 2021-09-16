import pygame

class conveyor_belt: 
    def __init__(self, positions:list[tuple]) -> None:
        self.positions = positions
        self.size = (20, 20) # px

    def draw_shape(self, surface:pygame.Surface):
        for p in self.positions:
            r = pygame.Rect(p, self.size)
            pygame.draw.rect(surface, [128, 128 , 128], r)

    def get_positions(self) -> list[tuple]:
        return self.positions.copy()

    def extend(self, new_positions:list[tuple]):
        self.positions.extend(new_positions)