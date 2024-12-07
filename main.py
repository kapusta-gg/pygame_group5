from models.zone import *


if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)

    dead_zone = DeadZone()
    main_zone = MainZone()
    spawn_zone = SpawnZone

    running = True
    while running:
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Отрисовка объектов
        dead_zone.draw(screen)
        main_zone.draw(screen)
        spawn_zone.draw(screen)
        # Обновление экрана
        pygame.display.flip()
