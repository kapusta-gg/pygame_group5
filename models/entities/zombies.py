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

        self.hp = 10

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image(Zombie.image), (100, 100))
        self.sprite.rect = self.zombie_hitbox
        self._ = pygame.sprite.GroupSingle()
        self._.add(self.sprite)

    def draw(self, screen: pygame.Surface, bullets_group, is_show_hitbox=True):
        self._.draw(screen)
        collide = pygame.sprite.spritecollideany(self.sprite, bullets_group, None)
        if collide:
            bullets_group.remove(collide)
            self.hp -= 1
        if self.hp <= 0:
            self._.empty()
            return
        if is_show_hitbox:
            pygame.draw.rect(screen, self.zombie_color, self.zombie_hitbox, width=2)

    def move(self, tick: float):
        self.x -= (Zombie.SPEED * tick) / 1000
        self.zombie_hitbox.x = self.x

