import pygame

import lib

class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.size = pygame.math.Vector2(width, height)

        self.image = pygame.Surface([self.size.x, self.size.y])
        self.image.fill(lib.color.gray)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        pass