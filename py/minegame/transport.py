import pygame
import time

import entity

class belt_piece:
    def __init__(self, pos:tuple) -> None:
        self.pos = pos
        self.holding_entity = None # holds entities

class conveyor_belt: 
    def __init__(self, positions:list[tuple]) -> None:
        self.UPDATE_INTERVAL = 200e6 # 200ms
        self.last_update = time.time_ns()

        self.pieces = []
        for p in positions:
            self.pieces.append(belt_piece(p))

        self.size = (20, 20) # px

    def draw_shape_with_materials(self, surface:pygame.Surface):
        for p in self.pieces:
            r = pygame.Rect(p.pos, self.size)
            pygame.draw.rect(surface, [128, 128 , 128], r)
            if p.holding_entity != None: p.holding_entity.draw_shape(p.pos, surface)

    def add_material(self, new_mat:entity) -> bool:
        if self.pieces[0].holding_entity == None:   # if space for new material-entity is available
            self.pieces[0].holding_entity = new_mat
            return True
        return False

    def move_materials(self) -> bool:
        one_gets_yeeted = False
        q = 0
        for p in self.pieces: 
            if p.holding_entity != None: 
                q += 1
        if time.time_ns() - self.last_update >= self.UPDATE_INTERVAL:
            self.last_update += self.UPDATE_INTERVAL

            for i in range(len(self.pieces), 0, -1):
                if i-1 < len(self.pieces) - 1:
                    if self.pieces[i].holding_entity == None:
                        self.pieces[i].holding_entity = self.pieces[i-1].holding_entity
                        self.pieces[i-1].holding_entity = None
                else:
                    if self.pieces[-1].holding_entity != None: one_gets_yeeted = self.pieces[-1]

            return one_gets_yeeted
            #todo what to do when belt ends?

    def is_first_piece_empty(self):
        return self.pieces[0].holding_entity == None #! belt must have a length >0

    # def get_positions(self) -> list[tuple]:
    #     return self.positions.copy()

    # def extend(self, new_positions:list[tuple]):
    #     self.positions.extend(new_positions)