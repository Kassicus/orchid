import pygame

class Color():
    def __init__(self):
        self.black = pygame.Color(0, 0, 0, 255)
        self.white = pygame.Color(255, 255, 255, 255)
        self.friendly = pygame.Color(0, 255, 100)
        self.friendly_highlight = pygame.Color(0, 255, 200)
        self.friendly_selected = pygame.Color(100, 255, 255)
        self.magenta = pygame.Color(255, 0, 255, 255)

color = Color()

window_size = pygame.math.Vector2(1000, 800)

deltatime = 0

events = None

mousemode = "select"

display_surface = None