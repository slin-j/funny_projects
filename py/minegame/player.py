import pygame

import transport
import resource_collect
import storage

class minegame_gamer():
    def __init__(self) -> None:
        self.conveyor_list = []
        self.miner_list = []
        self.storage_list = []

    def update_inout_interfaces(self):
        for m in self.miner_list: # miners
            m.update_spawner() 
            m.export_material_to_belt()
        for s in self.storage_list: # belts
            s.import_material_from_belt()
            s.export_material_to_belt()
        
    def draw_machine_shapes(self, surface:pygame.Surface):
        for c in self.conveyor_list: # belts
            c.draw_shape_with_materials(surface)
        for m in self.miner_list: # miners
            m.draw_shape(surface)
        for s in self.storage_list: # storage-containers
            s.draw_shape(surface)

    def is_pos_occupied(self, position:tuple):
        if position in [p for c in self.conveyor_list for p in c.get_piece_positions()]: # if pos contains any conveyorbelt piece
            return transport.conveyor_belt
        if position in [m.pos for m in self.miner_list]:
            return resource_collect.miner
        if position in [s.pos for s in self.storage_list]:
            return storage.storage_container
        return False

    def bind_belt_to_machine(self, belt:transport.conveyor_belt, insert_to_machine:bool, machine_pos):
        for machine in [m for m in self.miner_list] + [s for s in self.storage_list]:
            if machine.pos == machine_pos:
                if insert_to_machine == True:
                    machine.set_in_belt(belt, machine.pos)
                else:
                    machine.set_out_belt(belt, machine.pos)
