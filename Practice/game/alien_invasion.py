import pygame
import sys


class AlienInvasion:
    """Classe principal para gerir os recursos e comportamentos do jogo."""

    def __init__(self):
        """Inicializa o jogo e cria os recursos do jogo."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion - by Tomás Pacheco")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Inicializa o loop principal do jogo."""
        while True:

            # Observar os eventos de teclado e rato
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #pinta
            self.screen.fill(self.bg_color)
            # Redesenha o ecrã em cada passagem pelo loop
            pygame.display.flip()


if __name__ == '__main__':
    # Criar uma instância do jogo e executá-lo
    ai = AlienInvasion()
    ai.run_game()
