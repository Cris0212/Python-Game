import pygame
import sys

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.player_pos = [400, 550]  # Posición inicial del jugador
        self.player_speed = 5
        self.bullets = []  # Lista para almacenar las balas
        self.bullet_speed = 10

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def shoot(self):
        # Disparar una nueva bala
        bullet_pos = [self.player_pos[0] + 20, self.player_pos[1]]  # Ajusta la posición de la bala
        self.bullets.append(bullet_pos)

    def update_bullets(self):
        # Actualiza la posición de las balas
        for bullet in self.bullets:
            bullet[1] -= self.bullet_speed  # Mueve la bala hacia arriba

        # Elimina balas que están fuera de la pantalla
        self.bullets = [bullet for bullet in self.bullets if bullet[1] > 0]

    def run(self):
        while self.running:
            self.handle_events()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player_pos[0] > 0:
                self.player_pos[0] -= self.player_speed
            if keys[pygame.K_RIGHT] and self.player_pos[0] < 750:  # Ajustado para no salirse de la pantalla
                self.player_pos[0] += self.player_speed
            if keys[pygame.K_SPACE]:  # Dispara con la barra espaciadora
                self.shoot()
            if keys[pygame.K_m]:  # Para pausar la música
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            self.update_bullets()  # Actualiza la posición de las balas

            # Limpiar pantalla y dibujar
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (255, 0, 0), (self.player_pos[0], self.player_pos[1], 50, 50))  # Jugador

            # Dibujar balas
            for bullet in self.bullets:
                pygame.draw.rect(self.screen, (255, 255, 0), (bullet[0], bullet[1], 5, 10))  # Balas

            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
