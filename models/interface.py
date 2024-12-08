import pygame


class MainHUD:
    FONT_SIZE = 45

    def __init__(self):
        self.back = pygame.rect.Rect(0, 25, 900, 150)
        self.back_color = pygame.color.Color(255, 178, 102)

        self.cash = pygame.rect.Rect(5, 30, 120, 140)
        self.cash_color = pygame.color.Color(255, 204, 153)
        self.cash_font = pygame.font.Font(None, MainHUD.FONT_SIZE)
        self.cash_text = self.cash_font.render("10", True, (0, 0, 0))

        self.cards = pygame.rect.Rect(130, 30, 765, 140)
        self.cards_color = pygame.color.Color(255, 204, 153)
        self.cards_list = [PlantCard(135 + 127 * i, 35) for i in range(6)]

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.back_color, self.back,
                         border_bottom_left_radius=10, border_bottom_right_radius=10)

        pygame.draw.rect(screen, self.cash_color, self.cash, border_radius=10)
        screen.blit(self.cash_text, (self.cash.x, self.cash.y))

        pygame.draw.rect(screen, self.cards_color, self.cards, border_radius=10)
        for card in self.cards_list:
            card.draw(screen)


class PlantCard:
    FONT_SIZE = 30

    def __init__(self, x: int, y: int):
        self.back = pygame.rect.Rect(x, y, 120, 130)
        self.back_color = pygame.color.Color(255, 229, 204)
        self.cash_font = pygame.font.Font(None, PlantCard.FONT_SIZE)
        self.cash_text = self.cash_font.render("10", True, (0, 0, 0))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.back_color, self.back, border_radius=5)
        screen.blit(self.cash_text, (self.back.x, self.back.y))