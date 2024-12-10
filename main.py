import pygame.time

from models.zone import *
from models.interface import *
from models.entities.plants import *
from models.entities.zombies import *

if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)

    dead_zone = DeadZone()
    main_zone = MainZone()
    spawn_zone = SpawnZone()

    hud = MainHUD()

    #Тестовые
    plant = Plant(100, 200)
    zombie = Zombie(900, 200)

    clock = pygame.time.Clock()

    running = True
    isShowHitbox = True
    while running:
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                isShowHitbox = not isShowHitbox
        tick = clock.tick()
        # Логика
        zombie.move(10, tick)
        # Отрисовка объектов
        screen.fill((0, 0, 0))
        if isShowHitbox:
            dead_zone.draw(screen)
            main_zone.draw(screen)
            spawn_zone.draw(screen)
            plant.draw(screen)
            zombie.draw(screen)
        hud.draw(screen)
        # Обновление экрана
        pygame.display.flip()
