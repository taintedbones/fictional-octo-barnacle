import pygame
import random

WHITE = (255, 255, 255)


class VerticalPaddle:
    def __init__(self, x, y, width, height, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = surface

        self.start_x = x
        self.start_y = y
        self.start_rect_x = self.rect.x
        self.start_rect_y = self.rect.y

    def move_up(self):
        self.y -= self.velocity
        self.rect.y = self.y

    def move_down(self):
        self.y += self.velocity
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, (self.x, self.y, self.width, self.height))

    def reset(self):
        self.x = self.start_x
        self.y = self.start_rect_y
        self.rect.x = self.start_rect_x
        self.rect.y = self.start_rect_y

    def get_move(self, ball):
        r = random.randint(1,5)
        if r == 1:
            if ball.x < 400:
                if ball.y > self.rect.centery:
                    self.y += 1
                    self.rect.y += 1
                elif ball.y < self.rect.centery:
                    self.y -= 1
                    self.rect.y -= 1


class HorizontalPaddle:
    def __init__(self, x, y, width, height, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = surface

        self.start_x = x
        self.start_y = y
        self.start_rect_x = self.rect.x
        self.start_rect_y = self.rect.y

    def move_left(self):
        self.x -= self.velocity
        self.rect.x = self.x

    def move_right(self):
        self.x += self.velocity
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, (self.x, self.y, self.width, self.height))

    def reset(self):
        self.x = self.start_x
        self.y = self.start_rect_y
        self.rect.x = self.start_rect_x
        self.rect.y = self.start_rect_y

    def get_move(self, ball):
        r = random.randint(1, 5)
        if r == 1:
            if ball.x < 400:
                if ball.y > self.rect.centery:
                    self.y += 1
                    self.rect.y += 1
                elif ball.y < self.rect.centery:
                    self.y -= 1
                    self.rect.y -= 1