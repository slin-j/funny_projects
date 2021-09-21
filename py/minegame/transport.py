import os
import pygame
import time

import entity
import img_loader as img

def validate_belt_geometry(input:list):
    if len(input) == 0: return False
    if len(input) == 1: return True
    for i in range(len(input)-1):
        dx = abs(input[i][0]-input[i+1][0])
        dy = abs(input[i][1]-input[i+1][1])
        if (dx == 20 and dy == 0) or (dx == 0 and dy == 20): # valid if they are touching eachother on only one side
            continue
        if input.count(input[i]) >= 2: # duplicate
            return False
        if dx >= 20 or dy >= 20: # touching only on corner or not touching entirely
            return False
    return True

class interface_in:
    def __init__(self) -> None:
        self.in_pos = ()
        self.in_buffer = []
        self.in_buffer_size = 100
        self.in_belt = None

    def set_in_belt(self, belt, block_pos):
        self.in_belt = belt
        self.in_belt.out_block_pos = block_pos
        self.in_belt.update_belt_piece_img()

    def import_material_from_belt(self):
        if len(self.in_buffer) < self.in_buffer_size:
            e = self.in_belt.collect_entity()
            if e != None: self.in_buffer.append(e)

class interface_out:
    def __init__(self) -> None:
        self.out_pos = ()
        self.out_buffer = []
        self.out_buffer_size = 100
        self.out_belt = None

    def set_out_belt(self, belt, block_pos):
        self.out_belt = belt
        self.out_belt.in_block_pos = block_pos
        self.out_belt.update_belt_piece_img()

    # transfer entity from out_buffer to out_belt, if space is available and buffer not empty
    def export_material_to_belt(self):
        if len(self.out_buffer) >= 1 and self.out_belt.is_first_piece_empty() == True:
            self.out_belt.add_material(self.out_buffer.pop(0))
        return False

class belt_piece:
    def __init__(self, pos:tuple) -> None:
        self.pos = pos
        self.holding_entity = None # holds entities
        self.is_standing = False # only really needed for the last piece to ensure the collect only takes it when it waited there for one update-cycle
        self.belt_img_index = img.no_texture # index in the img_loader.belt list (graphic for this belt-piece)

class conveyor_belt: 
    def __init__(self, positions:list[tuple], tier:int) -> None:
        if tier > 0 and tier <= 5:
            self.tier = tier
            if self.tier == 1: self.UPDATE_INTERVAL = 1.000e9 # 60/min
            elif self.tier == 2: self.UPDATE_INTERVAL = 5.000e8 # 120/min
            elif self.tier == 3: self.UPDATE_INTERVAL = 2.222e8 # 270/min
            elif self.tier == 4: self.UPDATE_INTERVAL = 1.250e8 # 480/min
            elif self.tier == 5: self.UPDATE_INTERVAL = 7.692e7 # 780/min
        else: raise ValueError('Invalid belt tier! Valid are 1 to 5')
        self.last_update = time.time_ns()

        self.pieces = []
        for p in positions:
            self.pieces.append(belt_piece(p))

        # positions from the in and output-machine (used for belt-directions)
        self.in_block_pos = ()
        self.out_block_pos = ()

        self.update_belt_piece_img()

    def draw_shape_with_materials(self, surface:pygame.Surface):
        for p in self.pieces:
            # draw belt-pieces
            try: surface.blit(img.belt[p.belt_img_index], p.pos) # draw belt with the right texture (tier and direction matter)
            except IndexError: surface.blit(img.no_texture, p.pos) # you probably didnt run self.update_belt_piece_img() to update the images 
            # draw materials on belt
            if p.holding_entity != None: p.holding_entity.draw_shape(p.pos, surface)
            
    def update_belt_piece_img(self):
        a = 1
        for i,p in enumerate(self.pieces):
            if i == 0: # first -> use machine on the left
                p.belt_img_index = img.calculate_beltpiece_img([belt_piece(self.in_block_pos)] + self.pieces[:2], self.tier)
            elif i == len(self.pieces)-1: # last -> use machine on the right
                p.belt_img_index = img.calculate_beltpiece_img(self.pieces[-2:] + [belt_piece(self.out_block_pos)], self.tier)
            else:
                p.belt_img_index = img.calculate_beltpiece_img(self.pieces[i-1:i+2], self.tier)
            
    def add_material(self, new_mat:entity) -> bool:
        if self.pieces[0].holding_entity == None:   # if space for new material-entity is available
            self.pieces[0].holding_entity = new_mat
            return True
        return False

    # move materials by one position, if the waiting interval is over
    def move_materials(self) -> bool:
        if time.time_ns() - self.last_update >= self.UPDATE_INTERVAL:
            self.last_update += self.UPDATE_INTERVAL

            for i in range(len(self.pieces), 0, -1):
                if i-1 < len(self.pieces) - 1:
                    self.pieces[i-1].is_standing = False
                    if self.pieces[i].holding_entity == None:
                        self.pieces[i].holding_entity = self.pieces[i-1].holding_entity
                        self.pieces[i-1].holding_entity = None
                else:
                    if self.pieces[-1].holding_entity != None: 
                        self.pieces[-1].is_standing = True # ready to get collected by input

    def is_first_piece_empty(self):
        return self.pieces[0].holding_entity == None #! belt must have a length >0

    # lets you collect the entity on the last belt-piece
    def collect_entity(self):
        if self.pieces[-1].is_standing == True:
            e = self.pieces[-1].holding_entity
            self.pieces[-1].holding_entity = self.pieces[-2].holding_entity
            self.pieces[-1].is_standing = False
            return e
        return None
