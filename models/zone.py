import pygame


class MainZone:
    def __init__(self):
        self.main_zone_hitbox = pygame.rect.Rect(100, 200, 800, 600)
        self.main_zone_color = pygame.color.Color((0, 255, 0))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.main_zone_color, self.main_zone_hitbox, width=2)



class DeadZone:
    def __init__(self):
        self.dead_zone_hitbox = pygame.rect.Rect(0, 200, 100, 600)
        self.dead_zone_color = pygame.color.Color((255, 0, 0))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.dead_zone_color, self.dead_zone_hitbox, width=2)


class SpawnZone:
    def __init__(self):
        self.spawn_zone_hitbox = pygame.rect.Rect(900, 200, 100, 600)
        self.spawn_zone_color = pygame.color.Color((153, 0, 153))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.spawn_zone_color, self.spawn_zone_hitbox, width=2)