import pygame
import sys
import os

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('fonts', 'comicbd.ttf'), 32)
        self.background = pygame.image.load('images/background.png').convert()
        self.options = ["Jugar", "Scoreboard", "Salir"]
        self.selected_option = 0

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for index, option in enumerate(self.options):
            color = (255, 255, 255) if index == self.selected_option else (200, 200, 200)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (self.screen.get_width() / 2 - text.get_width() / 2, 200 + index * 50))
        
        pygame.display.update()

    def show(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return self.options[self.selected_option].lower()
