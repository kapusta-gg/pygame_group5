import pygame
from methods import load_image

X, Y = 0, 1


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

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        self._.draw(screen)
        if is_show_hitbox:
            pygame.draw.rect(screen, self.plant_color, self.plant_hitbox, width=2)

    def change_pos(self, x: int, y: int):
        self.plant_hitbox.x = x
        self.plant_hitbox.y = y