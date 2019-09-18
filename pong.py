import pygame
import sys
import random
from pygame.locals import *
from paddle import Paddle
import ball

# Set up window
WINDOWWIDTH = 800
WINDOWHEIGHT = 500

# ball class
# score class
# paddle class

# Color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pong No Wallzz')
top_p_paddle = Paddle(window_surface, 0, 90, 20, False)
side_p_paddle = Paddle(window_surface, 0, 20, 130, True)
bottom_p_paddle = Paddle(window_surface, 0, 90, WINDOWHEIGHT - 90, False)


def draw_dashed_line():
    dash_width = 5
    for y in range(40, WINDOWHEIGHT - 52, 30):
        pygame.draw.rect(window_surface, WHITE, (WINDOWWIDTH // 2 - 5, y, dash_width, 15), 0)


def draw_score(surface, text, x, y):
    font = pygame.font.Font(None, 35)
    text_render = font.render(text, True, WHITE, BLACK)

    text_rect = text_render.get_rect()
    text_rect.centerx = x + 100
    text_rect.centery = y + 30
    surface.blit(text_render, text_rect)


def initialize_screen():
    window_surface.fill(BLACK)
    draw_dashed_line()
    draw_score(window_surface, 'Player: ', 30, WINDOWHEIGHT - 60)
    draw_score(window_surface, 'Computer: ', WINDOWWIDTH - 300, WINDOWHEIGHT - 60)

    top_p_paddle.draw()
    side_p_paddle.draw()
    bottom_p_paddle.draw()

    pygame.mixer.music.load('House_short.ogg')
    pygame.mixer.music.play(-1)

    pygame.display.update()


def play_game():
    initialize_screen()

    # Runs game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # if event.type == KEYDOWN:
                # Update paddles to move down 1 unit in pos


play_game()
