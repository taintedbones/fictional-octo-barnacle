import pygame
import random


class Paddle:
    def __init__(self, surface, velocity, start_left_pos, start_top_pos, on_side):
        self.surface = surface
        self.bg_color = (255, 255, 255)
        self.width = 200
        self.height = 10
        self.on_side = on_side
        if on_side:
            self.rect = pygame.Rect(start_left_pos, start_top_pos, self.height, self.width)
        else:
            self.rect = pygame.Rect(start_left_pos, start_top_pos, self.width, self.height)
        self.surface_rect = surface.get_rect()
        self.velocity = velocity

    def update_pos(self, left_pos, top_pos):
        self.rect.move(left_pos, top_pos)

    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color, self.rect)
