import pygame

from models.zone import *
from models.interface import *
from models.entities.plants import *
from models.entities.zombies import *
from models.cursor import Cursor

if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)

    dead_zone = DeadZone()
    main_zone = MainZone()
    spawn_zone = SpawnZone()

    hud = MainHUD()

    cursor = Cursor()
    pygame.mouse.set_visible(False)

    #Тестовые
    zombies = []

    plant_to_place = None

    clock = pygame.time.Clock()

    running = True
    isShowHitbox = True
    isPlantCursor = False
    isDeleteCursor = False
    isMouseBlock = False

    while running:
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                isShowHitbox = not isShowHitbox
            if event.type == pygame.MOUSEBUTTONDOWN:
                if isDeleteCursor:
                    main_zone.check_pos_delete(event.pos)
                    isDeleteCursor = False
                elif isPlantCursor:
                    main_zone.check_pos_plant(event.pos, plant_to_place)
                    plant_to_place = None
                    isPlantCursor = False
                else:
                    on_cursor = hud.check_mouse_pos(event.pos)
                    if on_cursor is None:
                        pass
                    elif on_cursor == 1:
                        isDeleteCursor = True
                    else:
                        plant_to_place = on_cursor
                        isPlantCursor = True

            if event.type == pygame.MOUSEMOTION and isPlantCursor:
                plant_to_place.change_pos(*(i - 40 for i in event.pos))
            if event.type == pygame.MOUSEMOTION:
                cursor.move(*event.pos)
        tick = clock.tick()
        # Логика
        new_zombie = spawn_zone.spawn()
        if new_zombie is not None:
            zombies.append(new_zombie)
        bullets_group.update()
        print(len(zombies))
        zombies = [i for i in zombies if i.hp > 0]
        [zombie.move(tick) for zombie in zombies]
        # Отрисовка объектов
        screen.fill((100, 100, 100))
        dead_zone.draw(screen, is_show_hitbox=isShowHitbox)
        main_zone.draw(screen, is_show_hitbox=isShowHitbox)
        spawn_zone.draw(screen, is_show_hitbox=isShowHitbox)
        [zombie.draw(screen, bullets_group, is_show_hitbox=isShowHitbox) for zombie in zombies]
        bullets_group.draw(screen)
        hud.draw(screen)
        cursor.draw(screen)
        if plant_to_place is not None:
            plant_to_place.draw(screen, is_show_hitbox=isShowHitbox)
        # Обновление экрана
        pygame.display.flip()
