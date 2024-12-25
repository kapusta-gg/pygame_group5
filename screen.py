import pygame

from models.zone import *
from models.interface import *
from models.entities.plants import *
from models.entities.zombies import *
from models.cursor import Cursor


def game(screen):
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
                return 0
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


def main_screen(screen):
    clock = pygame.time.Clock()

    running = True

    button_game = pygame.rect.Rect(450, 375, 100, 50)
    close_game = pygame.rect.Rect(450, 450, 100, 50)

    while running:
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 450 <= x <= 550 and 375 <= y <= 425:
                   return 2
                elif 450 <= x <= 550 and 450 <= y <= 500:
                    return 0

        tick = clock.tick()
        # Логика

        # Отрисовка объектов
        pygame.draw.rect(screen, pygame.Color("green"), button_game)
        pygame.draw.rect(screen, pygame.Color("red"), close_game)
        # Обновление экрана
        pygame.display.flip()
