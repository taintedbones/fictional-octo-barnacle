import pygame
import random

WHITE = (255, 255, 255)


class VerticalPaddle:
    def __init__(self, x, y, width, height, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = surface

    def move_up(self):
        self.y -= self.velocity
        self.rect.y = self.y

    def move_down(self):
        self.y += self.velocity
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, (self.x, self.y, self.width, self.height))

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class HorizontalPaddle:
    def __init__(self, x, y, width, height, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = surface

    def move_left(self):
        self.x -= self.velocity
        self.rect.x = self.x

    def move_right(self):
        self.x += self.velocity
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, (self.x, self.y, self.width, self.height))

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y