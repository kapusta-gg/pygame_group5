import pygame
from methods import load_image

X, Y = 0, 1
bullets_group = pygame.sprite.Group()

class Plant:
    image = "images/plant.png"

    def __init__(self, x: int, y: int):
        self.plant_hitbox = pygame.rect.Rect(x, y, 100, 100)
        self.plant_color = pygame.color.Color((0, 0, 255))

        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.transform.scale(load_image(Plant.image), (100, 100))
        sprite.rect = self.plant_hitbox
        self._ = pygame.sprite.GroupSingle()
        self._.add(sprite)

        self.counter = 0

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        self._.draw(screen)
        if is_show_hitbox:
            pygame.draw.rect(screen, self.plant_color, self.plant_hitbox, width=2)

    def change_pos(self, x: int, y: int):
        self.plant_hitbox.x = x
        self.plant_hitbox.y = y

    def shoot(self):
        self.counter += 1
        if self.counter >= 100:
            bullets_group.add(Bullet(self.plant_hitbox.x, self.plant_hitbox.y))
            self.counter = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.rect = pygame.rect.Rect(x + 50, y + 50, 20, 20)
        self.image = pygame.transform.scale(load_image(Plant.image), (20, 20))

    def update(self):
        self.rect.x += 1