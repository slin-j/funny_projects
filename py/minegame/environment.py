import pygame 
import pygame_gui

class build_menu:
    def __init__(self, surface:pygame.display) -> None:
        self.visible = False
        self.surface = pygame.Surface((400,500)) # surface
        self.btn_manager = pygame_gui.UIManager((400,500))
        self.content = [
            pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (20, 20)), text='t1', manager=self.btn_manager),
            pygame_gui.elements.UIButton(relative_rect=pygame.Rect((40, 0), (20, 20)), text='t2', manager=self.btn_manager),
            pygame_gui.elements.UIButton(relative_rect=pygame.Rect((80, 0), (20, 20)), text='t3', manager=self.btn_manager)
        ]

    def draw_prompt(self, main_window:pygame.Surface):
        if self.visible == True:
            self.btn_manager.draw_ui(self.surface)
            main_window.blit(self.surface, (main_window.get_size()[0]/2 - (self.surface.get_size()[0]/2), 60))
            return True
        return False

    def set_visibility(self, vis:bool):
        self.visible = vis

    def handle_btn_pressed(self, dt):
        self.btn_manager.set_visual_debug_mode(True)
        rv = False

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.content[0]:
                        rv = 'belt_tier_1'
                    if event.ui_element == self.content[1]:
                        rv = 'belt_tier_2'
                    if event.ui_element == self.content[2]:
                        rv = 'belt_tier_3'

            self.btn_manager.process_events(event)
        self.btn_manager.update(dt)

        return rv

        # if element not in self.content:
        #     return False

        


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