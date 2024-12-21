import pygame
from methods import load_image


class Cursor:
    image = "images/cursor.png"

    # Изменить положение курсора
    def __init__(self):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image(Cursor.image)
        self.sprite.rect = self.sprite.image.get_rect()
        self._ = pygame.sprite.GroupSingle()
        self._.add(self.sprite)

    def move(self, x: int, y: int):
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    # Отрисовать курсор
    def draw(self, screen: pygame.Surface):
        self._.draw(screen)
