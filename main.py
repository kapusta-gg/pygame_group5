from models.zone import *


if __name__ == '__main__':
    pygame.init()
    size = w, h = 1000, 800
    screen = pygame.display.set_mode(size)

    main_zone = MainZone()

    running = True
    while running:
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Отрисовка объектов
        main_zone.draw(screen)

        # Обновление экрана
        pygame.display.flip()
