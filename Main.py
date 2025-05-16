import pygame
import sys
from menu import Menu
from game import Game
from scoreboard import Scoreboard

# Inicializar pygame
pygame.init()

# Establecer tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Cargar música
pygame.mixer.music.load('audios/background_music.mp3')  # Asegúrate de tener esta música
pygame.mixer.music.play(-1)  # Reproducir música en bucle

# Función principal
def main():
    menu = Menu(screen)
    game = Game(screen)
    scoreboard = Scoreboard(screen)

    while True:
        option = menu.show()
        if option == "jugar":
            game.run()
        elif option == "scoreboard":
            scoreboard.show()
        elif option == "salir":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()


