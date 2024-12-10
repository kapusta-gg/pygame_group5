import pygame

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

    plant_to_place = None

    clock = pygame.time.Clock()

    running = True
    isShowHitbox = True
    isPlantCursor = False
    isMouseBlock = False
    while running:
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                isShowHitbox = not isShowHitbox
            if event.type == pygame.MOUSEBUTTONDOWN:
                if isPlantCursor:
                    plant_to_place = None
                    isPlantCursor = False
                else:
                    plant_to_place = hud.check_mouse_pos(event.pos)
                    if plant_to_place is not None:
                        isPlantCursor = True

            if event.type == pygame.MOUSEMOTION and isPlantCursor:
                plant_to_place.change_pos(*(i - 40 for i in event.pos))
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
        if plant_to_place is not None:
            plant_to_place.draw(screen, is_hitbox=isShowHitbox)
        # Обновление экрана
        pygame.display.flip()
