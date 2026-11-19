import sys
import pygame
from settings import Settings
from bird import Bird


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
        self.background = pygame.transform.smoothscale(background, (new_w, self.settings.screen_height))
     

        self.bird = Bird(self)

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            self._check_events()
            self.bird.update()
            self._update_screen()
            self.relogio.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.bird.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.bird.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = False

    def _update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.bird.blitme()
        pygame.display.flip()



if __name__ == '__main__':
    pv = PassaroVoador()
    pv.run_game()
