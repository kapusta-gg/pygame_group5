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
    zombie = Zombie(900 ,200)

    running = True
    while running:
        # Просматриваем все события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Отрисовка объектов
        screen.fill((0, 0, 0))
        dead_zone.draw(screen)
        main_zone.draw(screen)
        spawn_zone.draw(screen)
        hud.draw(screen)

        plant.draw(screen)
        zombie.draw(screen)
        # Обновление экрана
        pygame.display.flip()
