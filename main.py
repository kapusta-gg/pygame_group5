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

    isShowHitbox = True
    isPlantOnCursor = False

    clock = pygame.time.Clock()

    plant_on_cursor = None

    #Тестовые
    plant = Plant(100, 200)
    zombie = Zombie(900, 200)

    running = True
    while running:
        tick = clock.tick()
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    isShowHitbox = not isShowHitbox

            if event.type == pygame.MOUSEBUTTONDOWN:
                plant_on_cursor = hud.check_mouse_pos(event.pos)
                if plant_on_cursor is not None:
                    isPlantOnCursor = True
                else:
                    isPlantOnCursor = False

            if event.type == pygame.MOUSEMOTION and isPlantOnCursor:
                plant_on_cursor.change_pos(event.pos)

        # Логика
        zombie.move(tick)
        # Отрисовка объектов
        screen.fill((0, 0, 0))
        hud.draw(screen)
        if isShowHitbox:
            dead_zone.draw(screen)
            main_zone.draw(screen)
            spawn_zone.draw(screen)
            plant.draw(screen)
            zombie.draw(screen)
            if plant_on_cursor is not None:
                plant_on_cursor.draw(screen)
        # Обновление экрана
        pygame.display.flip()
