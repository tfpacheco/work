import sys
import pygame
from settings import Settings
from bird import Bird
from obstacles import Obstacle


class PassaroVoador:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        pygame.display.set_caption("Passaro Voador")
        self.fonte = pygame.font.SysFont(None, 36)
        self.relogio = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        background = pygame.image.load(self.settings.screen_background_img).convert()
        bg_w, bg_h = background.get_size()
        scale = self.settings.screen_height / bg_h
        new_w = max(int(bg_w * scale), self.settings.screen_width)
        self.background = pygame.transform.smoothscale(
            background, (new_w, self.settings.screen_height))
        self.bg_w = self.background.get_width()

        self.bird = Bird(self)

        self.top_img = pygame.image.load('images/obs_down.png').convert_alpha()
        self.bottom_img = pygame.image.load('images/obs_up.png').convert_alpha()
        self.obs = pygame.sprite.Group()

        self.camera_x = 0.0
        self.next_obs_x = self.settings.screen_width  # onde nasce o próximo obstáculo (no mundo)

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            self._check_events()
            self.bird.update()
            self._update_world()
            self._update_screen()
            self.relogio.tick(60)

    def _update_world(self):
        # o pássaro avança no mundo e a câmara acompanha-o
        self.camera_x += self.settings.bird_speed_x

        # cria obstáculos à frente do pássaro
        while self.next_obs_x < self.camera_x + self.settings.screen_width:
            self.obs.add(Obstacle(self, self.next_obs_x,
                                  self.top_img, self.bottom_img))
            self.next_obs_x += self.settings.obs_distance

        self.obs.update(self.camera_x)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)

    def _keydown_events(self, event):
        if event.key in (pygame.K_SPACE, pygame.K_UP):
            self.bird.fly()
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        bg_x = -(self.camera_x % self.bg_w)
        self.screen.blit(self.background, (bg_x, 0))
        self.screen.blit(self.background, (bg_x + self.bg_w, 0))
        for obstacle in self.obs:
            obstacle.blitme()
        self.bird.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    pv = PassaroVoador()
    pv.run_game()
