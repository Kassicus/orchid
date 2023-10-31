import pygame
import math
import random

import lib

class Unit(pygame.sprite.Sprite):
    def __init__(self, target_x: int, target_y: int):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(target_x - random.randint(500, 800), random.randint(50, 750))
        self.vel = pygame.math.Vector2()

        self.target_pos = pygame.math.Vector2(target_x, target_y)

        self.speed = 200

        self.selected = False

        self.image = pygame.Surface([21, 21])
        self.image.fill(lib.color.friendly)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.vel = self.get_vectors()

    def get_vectors(self) -> list:
        distance = [self.target_pos.x - self.pos.x, self.target_pos.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = pygame.math.Vector2(rate[0] * self.speed, rate[1] * self.speed)

        return vectors
    
    def update(self):
        self.pos += self.vel * lib.deltatime
        self.rect.center = self.pos

        if self.pos.distance_to(self.target_pos) < 5:
            self.vel.x, self.vel.y = 0, 0

        self.check_selected()

        if self.selected:
            self.image.fill(lib.color.friendly_selected)

            if lib.mousemode == "move":
                if pygame.mouse.get_pressed()[0]:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.set_new_target(random.randint(mouse_x - 50, mouse_x + 50), random.randint(mouse_y - 50, mouse_y + 50))
                    self.selected = False

    def draw_debug(self):
        pygame.draw.line(lib.display_surface, lib.color.magenta, self.pos, self.target_pos)

    def check_selected(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.rect.left < mouse_x < self.rect.right:
            if self.rect.top < mouse_y < self.rect.bottom:
                self.image.fill(lib.color.friendly_highlight)

                if lib.mousemode == "select":
                    if pygame.mouse.get_pressed()[0]:
                        self.selected = True
            else:
                self.image.fill(lib.color.friendly)
        else:
            self.image.fill(lib.color.friendly)

    def set_new_target(self, x: int, y: int):
        self.target_pos.x, self.target_pos.y = x, y
        self.vel = self.get_vectors()