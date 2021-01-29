import pygame
import figures

class board():
    def __init__(self):
        pass

    def drawGrid(self,bg,start_x,start_y,field_dim):
        for y in range(8):
            for x in range(8):
                if (x + y) % 2:
                    rect = pygame.Rect(( (field_dim*x)+start_x, (field_dim*y)+start_y ), (field_dim,field_dim))   # (position),(dimension)
                    pygame.draw.rect(bg,(118,150,86),rect)
                else:
                    rect = pygame.Rect(( (field_dim*x)+start_x, (field_dim*y)+start_y ), (field_dim,field_dim))   # (position),(dimension)
                    pygame.draw.rect(bg,(238,238,210),rect)

    """def draw_figure(self, fig:figures):
        pass"""
