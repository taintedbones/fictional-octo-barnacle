import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Score:
    def __init__(self, x, y, player_type, surface):
        self.surface = surface;
        self.current_score = 0
        self.x = x
        self.y = y
        self.player_type = player_type

    def draw(self):
        font = pygame.font.Font(None, 35)
        text_render = font.render(self.player_type + ': ' + str(self.current_score), True, WHITE, BLACK)

        text_rect = text_render.get_rect()
        text_rect.centerx = self.x + 100
        text_rect.centery = self.y + 30
        self.surface.blit(text_render, text_rect)

    def scored(self):
        self.current_score += 1

    def reset(self):
        self.current_score = 0
