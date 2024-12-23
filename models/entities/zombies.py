import pygame
from methods import load_image
from models.entities.plants import Bullet


class Zombie:
    SPEED = 10
    image = "images/zombie.png"

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.zombie_hitbox = pygame.rect.Rect(self.x, self.y, 100, 100)
        self.zombie_color = pygame.color.Color((51, 0, 102))
        self.main_zone_line = None

        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.transform.scale(load_image(Zombie.image), (100, 100))
        sprite.rect = self.zombie_hitbox
        self._ = pygame.sprite.GroupSingle()
        self._.add(sprite)

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        self._.draw(screen)
        if is_show_hitbox:
            pygame.draw.rect(screen, self.zombie_color, self.zombie_hitbox, width=2)

    def move(self, tick: float):
        self.x -= (Zombie.SPEED * tick) / 1000
        self.zombie_hitbox.x = self.x

