import pygame 

class earth:
    def __init__(self, surface:pygame.display) -> None:
        self.bg = pygame.Surface(surface.get_size()).convert() # surface

    def draw_background(self):
        self.bg.fill([16,176,33])

    def draw_dbg_grid(self, SCR_WIDTH, SCR_HEIGHT):
        for y in range(0,int(SCR_WIDTH / 20)):
            for x in range(0,int(SCR_HEIGHT / 20)):
                if (x + y) % 2:
                    rect = pygame.Rect((20*x,20*y),(20,20))   # (position),(dimension)
                    pygame.draw.rect(self.bg,(152, 230, 66),rect)
                else:
                    rect = pygame.Rect((20*x,20*y),(20,20))   # (position),(dimension)
                    pygame.draw.rect(self.bg,(93, 230, 66),rect)