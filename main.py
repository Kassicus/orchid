import pygame
import random

import lib
import units
import debug

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.window_size.x, lib.window_size.y])
        pygame.display.set_caption("Project Orchid")

        lib.display_surface = self.screen

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get()

        self.debug_interface = debug.DebugInterface()

        self.units = pygame.sprite.Group()

    def start(self):
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for u in range(5):
                        u = units.Unit(random.randint(50, 300), random.randint(50, 750))
                        self.units.add(u)

                if event.key == pygame.K_s:
                    lib.mousemode = "select"
                
                if event.key == pygame.K_m:
                    lib.mousemode = "move"

                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

    def draw(self):
        self.screen.fill(lib.color.black)

        self.units.draw(self.screen)

        if self.debug_interface.active:
            self.debug_interface.draw(self.units)

    def update(self):
        self.units.update()

        self.debug_interface.update(self.clock)
        pygame.display.update()
        lib.deltatime = self.clock.tick(120) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()