import pygame
import random
from pygame.math import Vector2

BLACK = (0, 0, 0)
ball_image = pygame.image.load('pumpkin.jpg')


def vector2(xy_tuple, scale):
    v = Vector2()
    v[0], v[1] = xy_tuple[0], xy_tuple[1]
    return v * scale


class Ball:
    def __init__(self, x, y, width, height, velocity, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 10
        self.surface = surface;
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.move_x = velocity[0]
        self.move_y = velocity[1]

    def draw(self):
        pygame.draw.rect(self.surface, BLACK, self.rect)
        self.surface.blit(ball_image, (self.x, self.y))

    def move(self):
        self.x -= (self.velocity * (self.move_x / 10))
        self.y -= (self.velocity * (self.move_y / 10))
        self.rect.topleft = self.x, self.y

    def collision(self, h_paddles, v_paddles):
        r = self.rect

        if r.colliderect(h_paddles[0]) or r.colliderect(h_paddles[1]):
            self.move_x *= -1
            self.velocity += 0.2

        if r.colliderect(v_paddles[0]) or r.colliderect(v_paddles[1]) or r.colliderect(v_paddles[2]):
            self.move_y *= -1
            self.velocity += 0.2
