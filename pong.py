import pygame
import sys
import random
from pygame.locals import *

pygame.init()
main_clock = pygame.time.Clock()

# Set up window
WINDOWWIDTH = 700
WINDOWHEIGHT = 400
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pong No Wallzz')

# ball class
# score class
# paddle class

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_dashed_line():
    for y in range(40, WINDOWHEIGHT - 52, 30):
        pygame.draw.rect(window_surface, WHITE, (WINDOWWIDTH // 2 - 5, y, 10, 15), 0)


def initialize_screen():
    window_surface.fill(BLACK)
    draw_dashed_line()
    pygame.display.update()


def play_game():
    # Runs game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


initialize_screen()
play_game()
