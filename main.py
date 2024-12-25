import pygame

from screen import game, main_screen

screen_dict = {1: main_screen,
               2: game}


if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)
    screen_id = 1

    # screen_id == 0 (логический False) => конец игры
    while screen_id:
        screen_id = screen_dict[screen_id](screen)

