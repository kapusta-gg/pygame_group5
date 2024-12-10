import pygame


class Plant:
    def __init__(self, x: int, y: int):
        self.plant_hitbox = pygame.rect.Rect(x, y, 100, 100)
        self.plant_color = pygame.color.Color((0, 0, 255))

    def draw(self, screen: pygame.Surface, is_hitbox=True):
        if is_hitbox:
            pygame.draw.rect(screen, self.plant_color, self.plant_hitbox, width=2)