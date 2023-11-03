import pygame
import math
import random

import lib

class Unit(pygame.sprite.Sprite):
    def __init__(self, team: str):
        pygame.sprite.Sprite.__init__(self)

        self.team = team

        self.pos = pygame.math.Vector2()
        self.move_target_pos = pygame.math.Vector2()

        if self.team == "a":
            self.pos.x = random.randint(-800, -500)
            self.move_target_pos.x = random.randint(50, 300)
        elif self.team == "b":
            self.pos.x = random.randint(int(lib.window_size.x) + 500, int(lib.window_size.x) + 800)
            self.move_target_pos.x = random.randint(int(lib.window_size.x) - 300, int(lib.window_size.x) - 50)
        self.pos.y = random.randint(50, 750)
        self.move_target_pos.y = random.randint(50, 750)

        self.vel = pygame.math.Vector2()

        self.speed = 200
        self.range = 150
        self.color_set = []

        if self.team == "a":
            self.color_set.append(lib.color.friendly)
            self.color_set.append(lib.color.friendly_highlight)
            self.color_set.append(lib.color.friendly_selected)
        elif self.team == "b":
            self.color_set.append(lib.color.enemy)
            self.color_set.append(lib.color.enemy_highlight)
            self.color_set.append(lib.color.enemy_selected)

        self.selected = False

        self.image = pygame.Surface([21, 21])
        self.image.fill(self.color_set[0])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.vel = self.get_vectors()

    def get_vectors(self) -> list:
        distance = [self.move_target_pos.x - self.pos.x, self.move_target_pos.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = pygame.math.Vector2(rate[0] * self.speed, rate[1] * self.speed)

        return vectors
    
    def update(self):
        self.pos += self.vel * lib.deltatime
        self.rect.center = self.pos

        if self.pos.distance_to(self.move_target_pos) < 5:
            self.vel.x, self.vel.y = 0, 0

        self.check_selected()

        if self.selected:
            self.image.fill(self.color_set[2])

            if lib.mousemode == "move":
                if pygame.mouse.get_pressed()[0]:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.set_new_move_target(random.randint(mouse_x - 50, mouse_x + 50), random.randint(mouse_y - 50, mouse_y + 50))
                    self.selected = False

        self.target_enemy()

    def draw_debug(self):
        pygame.draw.line(lib.display_surface, lib.color.magenta, self.pos, self.move_target_pos)

        pygame.draw.circle(lib.display_surface, lib.color.white, self.pos, self.range, 1)

    def check_selected(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.rect.left < mouse_x < self.rect.right:
            if self.rect.top < mouse_y < self.rect.bottom:
                self.image.fill(self.color_set[1])

                if lib.mousemode == "select":
                    if pygame.mouse.get_pressed()[0]:
                        self.selected = True
            else:
                self.image.fill(self.color_set[0])
        else:
            self.image.fill(self.color_set[0])

    def set_new_move_target(self, x: int, y: int):
        self.move_target_pos.x, self.move_target_pos.y = x, y
        self.vel = self.get_vectors()

    def target_enemy(self):
        pass