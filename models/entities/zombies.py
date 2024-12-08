import pygame


class Zombie:
    def __init__(self, x: int, y: int):
        self.zombie_hitbox = pygame.rect.Rect(x, y, 100, 100)
        self.zombie_color = pygame.color.Color((51, 0, 102))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.zombie_color, self.zombie_hitbox, width=2)