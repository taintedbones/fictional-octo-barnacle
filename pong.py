import pygame
import sys
import random
from pygame.locals import *
from paddle import *
import ball

# Set up window
WINDOWWIDTH = 800
WINDOWHEIGHT = 500
BALLSPEED = 3
PADDLESPEED = 5

# ball class
# score class
# paddle class

# Color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pong No Wallzz')
p_top_paddle = HorizontalPaddle(90, 20, 100, 10, window_surface)
p_bottom_paddle = HorizontalPaddle(90, WINDOWHEIGHT - 90, 100, 10, window_surface)
p_side_paddle = VerticalPaddle(20, 130, 10, 100, window_surface)

move_left = move_right = move_up = move_down = False

pygame.mixer.music.load('House_short.ogg')
pygame.mixer.music.play(-1)


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

    p_top_paddle.draw()
    p_side_paddle.draw()
    p_bottom_paddle.draw()

    pygame.display.update()


def play_game():
    initialize_screen()

    # Runs game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN or event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_a:
                    if p_top_paddle.x > 0:
                        p_top_paddle.move_left()
                        p_bottom_paddle.move_left()
                if event.key == K_RIGHT or event.key == K_d:
                    if p_top_paddle.x < WINDOWWIDTH:
                        p_top_paddle.move_right()
                        p_bottom_paddle.move_right()
                if event.key == K_UP or event.key == K_w:
                    if p_side_paddle.y > 0:
                        p_side_paddle.move_up()
                if event.key == K_DOWN or event.key == K_s:
                    if p_side_paddle.y < WINDOWHEIGHT - p_side_paddle.height:
                        p_side_paddle.move_down()
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # if event.type == KEYUP:
            #     if event.key == K_ESCAPE:
            #         pygame.quit()
            #         sys.exit()
            #     if event.key == K_LEFT or event.key == K_a:
            #         p_top_paddle.move_left()
            #         p_bottom_paddle.move_left()
            #     if event.key == K_RIGHT or event.key == K_d:
            #         p_top_paddle.move_right()
            #         p_bottom_paddle.move_right()
            #     if event.key == K_UP or event.key == K_w:
            #         p_side_paddle.move_up()
            #     if event.key == K_DOWN or event.key == K_s:
            #         p_side_paddle.move_down()

        initialize_screen()
        pygame.display.update()


play_game()
