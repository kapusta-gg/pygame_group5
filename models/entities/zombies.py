import pygame
import math

class Zombie:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.zombie_hitbox = pygame.rect.Rect(self.x, self.y, 100, 100)
        self.zombie_color = pygame.color.Color((51, 0, 102))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.zombie_color, self.zombie_hitbox, width=2)

    def move(self, speed, tick):
        print(self.zombie_hitbox.x, self.zombie_hitbox.y)
        self.x += -speed * tick / 1000
        self.zombie_hitbox = pygame.rect.Rect(int(self.x), self.y, 100, 100)