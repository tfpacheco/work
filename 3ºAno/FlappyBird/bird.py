import pygame
from pygame.sprite import Sprite


class Bird(Sprite):
    def __init__(self, pv_game):
        super().__init__()
        self.screen = pv_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pv_game.settings

      
        self.image = pygame.image.load('images/bird.png')
        self.image = pygame.transform.scale(self.image, (150, 100))  # (largura, altura)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    
        
        self.x = float(self.rect.x)
       
        self.rect.centery = self.screen_rect.centery
        self.rect.x = 20
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.bird_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.bird_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    
