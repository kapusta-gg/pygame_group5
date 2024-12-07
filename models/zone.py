import pygame


class MainZone:
    def __init__(self):
        self.main_zone_hitbox = pygame.rect.Rect(100, 200, 800, 600)
        self.main_zone_color = pygame.color.Color((0, 255, 0))

    def draw(self, screen):
        pygame.draw.rect(screen, self.main_zone_color, self.main_zone_hitbox, width=2)


class DeadZone:
    pass


class SpawnZone:
    pass