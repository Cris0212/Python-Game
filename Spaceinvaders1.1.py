import pygame
import random
import math
import os
import sys

# Inicializar pygame
pygame.init()

# Establecer el tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Función para obtener los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Cargar imagen de fondo
asset_background = resource_path('images/background.png')
background = pygame.image.load(asset_background)

# Cargar icono de ventana
asset_icon = resource_path('images/ufo.png')
icon = pygame.image.load(asset_icon)

# Cargar sonido de fondo
asset_sound = resource_path('audios/background_music.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

# Cargar imagen del jugador
asset_playerimg = resource_path('images/space-invaders.png')
playerimg = pygame.image.load(asset_playerimg)

# Cargar imagen de la bala
asset_bulletimg = resource_path('images/bullet.png')
bulletimg = pygame.image.load(asset_bulletimg)

# Cargar imagen de los enemigos
enemy_img_path1 = resource_path('images/enemy1.png')
enemy_img_path2 = resource_path('images/enemy2.png')

# Cargar fuente para texto game over
asset_over_font = resource_path('fonts/RAVIE.TTF')
over_font = pygame.font.Font(asset_over_font, 64)

# Cargar fuente para el puntaje
asset_font = resource_path('fonts/comicbd.ttf')
font = pygame.font.Font(asset_font, 32)

# Establecer título de ventana
pygame.display.set_caption("Space Invaders")

# Establecer icono de la ventana
pygame.display.set_icon(icon)

# Reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

# Crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Posición inicial del jugador
playerX = 370
playerY = 470
playerX_change = 0

# Lista para almacenar las posiciones de los enemigos
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

# Se inicializa las variables para obtener las posiciones de los enemigos
for i in range(no_of_enemies):
    # Alternar entre las dos imágenes de los enemigos
    if i % 2 == 0:
        enemyimg.append(pygame.image.load(enemy_img_path1))
    else:
        enemyimg.append(pygame.image.load(enemy_img_path2))
    
    # Se asigna una posición aleatoria en X y Y para el enemigo
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))

    # Se establece la velocidad de movimiento del enemigo de x y y
    enemyX_change.append(4.5)  # Velocidad 4.5
    enemyY_change.append(20)

# Se inicializan las variables para guardar la posición de la bala
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "Ready"

# Se inicializa la puntuación en 0
score = 0

# Función para mostrar la puntuación en pantalla
def show_score():
    score_value = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (10, 10))

# Función para dibujar al jugador en la pantalla
def player(x, y):
    screen.blit(playerimg, (x, y))

# Función para dibujar el enemigo en la pantalla
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

# Función para disparar la bala
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletimg, (x + 16, y + 10))

# Función para comprobar si ha habido una colisión entre la bala y el enemigo
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27

# Función para mostrar el texto game over en pantalla
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(over_text, text_rect)

# Función para mostrar el nombre del jugador y el puntaje
def show_final_score(name):
    final_text = font.render(f"{name}, tu puntuación es: {score}", True, (255, 255, 255))
    text_rect = final_text.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
    screen.blit(final_text, text_rect)

# Función para la pantalla de inicio
def start_screen():
    global player_name
    input_active = True
    player_name = ""
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
        
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        
        title = font.render("Space Invaders", True, (255, 255, 255))
        screen.blit(title, (screen_width / 2 - title.get_width() / 2, 50))

        instructions = font.render("Ingresa tu nombre y presiona Enter", True, (255, 255, 255))
        screen.blit(instructions, (screen_width / 2 - instructions.get_width() / 2, 150))
        
        name_text = font.render(player_name, True, (255, 255, 255))
        screen.blit(name_text, (screen_width / 2 - name_text.get_width() / 2, 200))
        
        pygame.display.update()

# Función para mostrar el menú de fin de juego
def end_screen():
    global score
    in_menu = True
    while in_menu:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        game_over_text()
        show_final_score(player_name)
        
        restart_text = font.render("Presiona R para volver al Menú o Q para Salir", True, (255, 255, 255))
        text_rect = restart_text.get_rect(center=(screen_width / 2, screen_height / 2 + 100))
        screen.blit(restart_text, text_rect)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_screen()  # Volver al menú inicial
                    in_menu = False  # Salir del menú
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Función para reiniciar el juego
def reset_game():
    global score, playerX, playerY, playerX_change, bulletX, bulletY, bullet_state
    score = 0
    playerX = 370
    playerY = 470
    playerX_change = 0
    bulletX = 0
    bulletY = 480
    bullet_state = "Ready"
    
    # Reiniciar enemigos
    for i in range(no_of_enemies):
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(50, 150)

# Función principal del juego
def gameloop():
    global score
    global playerX
    global playerX_change
    global bulletX
    global bulletY
    global bullet_state

    in_game = True
    while in_game:
        # Maneja eventos, actualiza y renderiza el juego
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Maneja el movimiento del jugador y el disparo
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "Ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_m:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Actualizar posición del jugador
        playerX += playerX_change
        playerX = max(0, min(playerX, screen_width - 64))  # Mantener al jugador en la pantalla

        # Actualizar posición de los enemigos
        for i in range(no_of_enemies):
            # Comprobar colisiones
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "Ready"
                score += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4.5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4.5
                enemyY[i] += enemyY_change[i]

            # Comprobar si el juego ha terminado
            if enemyY[i] > playerY:
                in_game = False
                break
            
            # Dibujar al enemigo
            enemy(enemyX[i], enemyY[i], i)

        # Actualizar posición de la bala
        if bullet_state == "Fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "Ready"

        # Dibujar al jugador
        player(playerX, playerY)

        # Mostrar puntuación
        show_score()

        pygame.display.update()
        
    end_screen()

# Pantalla de inicio
start_screen()

# Iniciar el bucle del juego
gameloop()
