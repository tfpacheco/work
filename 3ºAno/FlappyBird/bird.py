import pygame
from pygame.sprite import Sprite


class Bird(Sprite):
    def __init__(self, pv_game):
        super().__init__()
        self.screen = pv_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pv_game.settings

        self.image = pygame.image.load('images/bird.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)
        self.velocity = 0.0

    def fly(self):
        self.velocity = -self.settings.bird_jump

    def update(self):
        self.velocity += self.settings.gravity
        self.y += self.velocity

        if self.y < 0:
            self.y = 0
            self.velocity = 0
        max_y = self.screen_rect.bottom - self.rect.height
        if self.y > max_y:
            self.y = max_y
            self.velocity = 0

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
