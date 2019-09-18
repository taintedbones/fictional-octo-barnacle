import pygame
import random
from pygame.sprite import Sprite

ball_image = pygame.image.load('pumpkin.jpg')


class Ball(Sprite):
    def __init__(self, surface, start_speed, acceleration):
        # Calls the base class, same as pygame.sprite.Sprite.__init__(self)
        super(Ball, self).__init__()
        self.surface = surface
        self.surface_rect = surface.get_rect()

        self.rect = pygame.Rect(0, 0, 20, 20)
        self.rect.center = self.surface_rect.center

        self.ball_start_speed = 10
        self.ball_acceleration = 5
        self.ball_angular
        # ball hit sound

        rand_vel = random.uniform(-self.ball_start_speed, self.ball_start_speed)
        self.velocity_x = rand_vel
        self.velocity_y = self.ball_start_speed - abs(rand_vel)

        self.last_paddle_collided_with = None

    def calculate_horizontal_collision(self, collision):
        if collision:
            if collision != self.last_paddle_collided_with:
                self.last_paddle_collided_with = collision
                self.velocity_x *= -1
                difference = self.rect.centery - collision.rect.centery
                velocity_change_amount = difference * self.ball_angular
                self.velocity_y += velocity_change_amount

    def calculate_vertical_collision(self):
        if collision:
            if collision != self.last_paddle_collided_with:
                self.last_paddle_collided_with = collision
                self.velocity_y *= -1
                difference = self.rect.centery - collision.rect.centery
                velocity_change_amount = difference * self.ball_angular
                self.velocity_x += velocity_change_amount

    def update(self, paddles):
        self.velocity_x += self.ball_acceleration if self.velocity_x > 0 else -self.ball_acceleration
        self.center_x += self.velocity_x
        self.rect.centerx = self.center_x

        collision = pygame.sprite.spritecollideany(self, paddles)
        self.calcutate_horizontal_collision(collision)
        self.velocity_y += self.ball_acceleration if self.velocity_y > 0 else -self.ball_acceleration
        self.center_y += self.velocity_y
        self.rect.centery = self.center_y

        collision = pygame.sprite.spritecollideany(self, paddles)
        self.calculate_vertical_collision(collision)

    def draw(self, color):

        pygame.draw.Rect(self.surface, color, self.rect)