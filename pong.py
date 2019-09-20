import pygame
import sys
import random
from pygame.locals import *
from paddle import *
from ball import *
from score import *

# Set up window
WINDOWWIDTH = 800
WINDOWHEIGHT = 500
BALLSPEED = 3
PADDLESPEED = 5
WINNINGSCORE = 2
in_play = True

# Color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pong No Wallzz')

ball = Ball(WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 20, 20, (0, 2), window_surface)

p_top_paddle = HorizontalPaddle(90, 20, 100, 10, window_surface)
p_bottom_paddle = HorizontalPaddle(90, WINDOWHEIGHT - 90, 100, 10, window_surface)
p_side_paddle = VerticalPaddle(20, 130, 10, 100, window_surface)

c_top_paddle = HorizontalPaddle(WINDOWWIDTH - 150, 20, 100, 10, window_surface)
c_bottom_paddle = HorizontalPaddle(WINDOWWIDTH - 150, WINDOWHEIGHT - 90, 100, 10, window_surface)
c_side_paddle = VerticalPaddle(WINDOWWIDTH - 30, 130, 10, 100, window_surface)

p_score = Score(30, WINDOWHEIGHT - 60, 'Player', window_surface)
c_score = Score(WINDOWWIDTH - 300, WINDOWHEIGHT - 60, 'Computer', window_surface)

move_left = move_right = move_up = move_down = False

pygame.mixer.music.load('House_short.ogg')
pygame.mixer.music.play(-1)


def draw_dashed_line():
    dash_width = 5
    for y in range(40, WINDOWHEIGHT - 52, 30):
        pygame.draw.rect(window_surface, WHITE, (WINDOWWIDTH // 2 - 5, y, dash_width, 15), 0)


def check_scores():
    game_over = False

    if p_score.current_score == WINNINGSCORE:
        text = 'You won!'
        game_over = True
    elif c_score.current_score == WINNINGSCORE:
        text = 'You lose!'
        game_over = True

    if game_over:
        in_play = False
        p_score.reset()
        c_score.reset()
        window_surface.fill(BLACK)
        font = pygame.font.Font(None, 35)
        game_over_msg = font.render(text, True, WHITE)
        window_surface.blit(game_over_msg, window_surface.get_rect())
        pygame.display.update()


def update_screen():
    window_surface.fill(BLACK)
    draw_dashed_line()

    p_score.draw()
    c_score.draw()

    p_top_paddle.draw()
    p_side_paddle.draw()
    p_bottom_paddle.draw()

    c_top_paddle.draw()
    c_side_paddle.draw()
    c_bottom_paddle.draw()

    ball.draw()
    ball.move()

    pygame.display.update()


def play_game():
    update_screen()

    h_paddles = []
    v_paddles = []

    h_paddles.append(p_top_paddle)
    h_paddles.append(p_bottom_paddle)
    h_paddles.append(c_top_paddle)
    h_paddles.append(c_bottom_paddle)
    v_paddles.append(p_side_paddle)
    v_paddles.append(c_side_paddle)



    # Runs game loop
    while True:

        check_scores()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN or event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_a:
                    if p_top_paddle.x > 0:
                        p_top_paddle.move_left()
                        p_bottom_paddle.move_left()
                elif event.key == K_RIGHT or event.key == K_d:
                    if p_top_paddle.x < WINDOWWIDTH:
                        p_top_paddle.move_right()
                        p_bottom_paddle.move_right()
                elif event.key == K_UP or event.key == K_w:
                    if p_side_paddle.y > 0:
                        p_side_paddle.move_up()
                elif event.key == K_DOWN or event.key == K_s:
                    if p_side_paddle.y < WINDOWHEIGHT - p_side_paddle.height:
                        p_side_paddle.move_down()
                elif event.key == K_ESCAPE:
                    pygame.quit()

        update_screen()
        c_top_paddle.get_move(ball.rect)
        c_bottom_paddle.get_move(ball.rect)
        c_side_paddle.get_move(ball.rect)

        ball.draw()
        ball.move()
        ball.collision(h_paddles, v_paddles)
        scored_reset, scorer = ball.reset()

        if scored_reset:
            if scorer == 'Player':
                p_score.scored()
            elif scorer == 'Computer':
                c_score.scored()

            p_top_paddle.reset()
            p_bottom_paddle.reset()
            p_side_paddle.reset()
            c_top_paddle.reset()
            c_bottom_paddle.reset()
            c_side_paddle.reset()
            update_screen()



        pygame.display.update()


play_game()
