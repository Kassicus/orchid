import pygame

import lib

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.window_size.x, lib.window_size.y])
        pygame.display.set_caption("Project Orchid")

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get()

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

    def draw(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        pygame.display.update()
        lib.deltatime = self.clock.tick(120) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()