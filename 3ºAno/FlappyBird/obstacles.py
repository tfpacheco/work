import random
import pygame
from pygame.sprite import Sprite


class Obstacle(Sprite):
    """Par de obstáculos (um em cima e outro em baixo)."""

    def __init__(self, pv_game, world_x, top_img, bottom_img):
        super().__init__()
        self.screen = pv_game.screen
        self.settings = pv_game.settings

        screen_height = self.screen.get_height()
        gap = self.settings.obs_gap
        width = self.settings.obs_width

        gap_y = random.randint(100, screen_height - 100 - gap)
        top_h = gap_y
        bottom_h = screen_height - (gap_y + gap)

        self.top_image = pygame.transform.scale(top_img, (width, top_h))
        self.bottom_image = pygame.transform.scale(bottom_img, (width, bottom_h))

        self.world_x = float(world_x)
        self.top_rect = self.top_image.get_rect(topleft=(world_x, 0))
        self.bottom_rect = self.bottom_image.get_rect(topleft=(world_x, gap_y + gap))

    def update(self, camera_x):
        screen_x = self.world_x - camera_x
        self.top_rect.x = screen_x
        self.bottom_rect.x = screen_x
        if self.top_rect.right < 0:
            self.kill()

    def collides(self, rect):
        return (self.top_rect.colliderect(rect)
                or self.bottom_rect.colliderect(rect))

    def blitme(self):
        self.screen.blit(self.top_image, self.top_rect)
        self.screen.blit(self.bottom_image, self.bottom_rect)
