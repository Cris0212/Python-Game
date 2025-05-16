import pygame
import os
import sys

class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('fonts', 'comicbd.ttf'), 32)
        self.background = pygame.image.load('images/background.png').convert()

    def show(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            # Aquí puedes mostrar los puntajes
            text = self.font.render("Puntajes", True, (255, 255, 255))
            self.screen.blit(text, (self.screen.get_width() / 2 - text.get_width() / 2, 50))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Regresar al menú
                        return
