import pygame

import lib

class DebugInterface():
    def __init__(self):
        self.active = False

        self.font = pygame.font.SysFont("Courier", 16)

        self.offset = 10

        self.t_fps = None
        self.t_mouse = None
        self.t_mousemode = None

        self.o_fps = None
        self.o_mouse = None
        self.o_mousemode = None

    def get_fps(self, clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        string = "FPS: " + str(int(clock.get_fps()))
        text = self.font.render(string, True, lib.color.magenta)

        offset = int(lib.window_size.x - text.get_width() - self.offset)

        return text, offset
    
    def get_mouse(self) -> list [pygame.Surface, int]:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        string = "Mouse: " + str(mouse_x) + "," + str(mouse_y)
        text = self.font.render(string, True, lib.color.magenta)

        offset = int(lib.window_size.x - text.get_width() - self.offset)

        return text, offset
    
    def get_mousemode(self) -> list [pygame.Surface, int]:
        string = "Mousemode: " + str(lib.mousemode)
        text = self.font.render(string, True, lib.color.magenta)

        offset = int(lib.window_size.x - text.get_width() - self.offset)

        return text, offset
    
    def toggle_active(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self, unit_group: pygame.sprite.Group):
        lib.display_surface.blit(self.t_fps, (self.o_fps, 10))
        lib.display_surface.blit(self.t_mouse, (self.o_mouse, 30))
        lib.display_surface.blit(self.t_mousemode, (self.o_mousemode, 50))

        for unit in unit_group:
            unit.draw_debug()

    def update(self, clock: pygame.time.Clock):
        self.t_fps, self.o_fps = self.get_fps(clock)
        self.t_mouse, self.o_mouse = self.get_mouse()
        self.t_mousemode, self.o_mousemode = self.get_mousemode()