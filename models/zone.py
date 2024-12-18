import pprint
from models.entities.plants import *
from models.entities.zombies import *
import pygame
import random


class MainZone:
    def __init__(self):
        self.main_zone_hitbox = pygame.rect.Rect(100, 200, 800, 600)
        self.main_zone_color = pygame.color.Color((0, 255, 0))
        self.board = [[None] * 8 for _ in range(6)]

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.main_zone_color, self.main_zone_hitbox, width=2)
            for i in range(8):
                for j in range(6):
                    if self.board[j][i] is not None:
                        self.board[j][i].draw(screen, is_show_hitbox=is_show_hitbox)
                    else:
                        rect = pygame.rect.Rect(100 + i * 100, 200 + j * 100, 100, 100)
                        pygame.draw.rect(screen, self.main_zone_color, rect, width=2)

    def check_pos_plant(self, pos: tuple[int, int], plant: Plant):
        x = (pos[0] - 100) // 100
        y = (pos[1] - 200) // 100
        ch_x = 0 <= x < 8
        ch_y = 0 <= x < 6
        if ch_x and ch_y:
            plant.plant_hitbox.x = 100 + x * 100
            plant.plant_hitbox.y = 200 + y * 100
            self.board[y][x] = plant

    def check_pos_delete(self, pos: tuple[int, int]):
        x = (pos[0] - 100) // 100
        y = (pos[1] - 200) // 100
        ch_x = 0 <= x < 8
        ch_y = 0 <= x < 6
        if ch_x and ch_y:
            self.board[y][x] = None


class DeadZone:
    def __init__(self):
        self.dead_zone_hitbox = pygame.rect.Rect(0, 200, 100, 600)
        self.dead_zone_color = pygame.color.Color((255, 0, 0))

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.dead_zone_color, self.dead_zone_hitbox, width=2)


class SpawnZone:
    def __init__(self):
        self.spawn_zone_hitbox = pygame.rect.Rect(900, 200, 100, 600)
        self.spawn_zone_color = pygame.color.Color((153, 0, 153))
        self.counter = 0

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.spawn_zone_color, self.spawn_zone_hitbox, width=2)

    def spawn(self):
        self.counter += 1
        if self.counter >= 2000:
            line = random.randint(0, 6)
            self.counter = 0
            return Zombie(900, 200 + line * 100)