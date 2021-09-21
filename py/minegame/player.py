import pygame

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