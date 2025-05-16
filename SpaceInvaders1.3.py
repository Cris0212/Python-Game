import pygame
import random
import math
import os
import sys

# Inicializar pygame
pygame.init()

# Establece el tamaño de la pantalla
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
        enemy_img_path = resource_path("images/enemy1.png")
    else:
        enemy_img_path = resource_path("images/enemy2.png")
    enemyimg.append(pygame.image.load(enemy_img_path))

    # Se asigna una posición aleatoria en X y Y para el enemigo
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))

    # Se establece la velocidad de movimiento del enemigo de x y y
    enemyX_change.append(5)
    enemyY_change.append(20)

# Se inicializan las variables para guardar la posición de la bala
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "Ready"

# Se inicializa la puntuación en 0
score = 0

# Variables de temporizador y velocidad
timer = 0
game_speed = 5  # Velocidad inicial
last_time = pygame.time.get_ticks()  # Tiempo del último incremento de velocidad
speed_increment_time = 10000  # Incrementar cada 10 segundos
music_paused = False  # Estado de la música

# Función para mostrar la puntuación en pantalla
def show_score():
    score_value = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (10, 10))

# Función para dibujar al jugador en la pantalla
def player(x, y):
    screen.blit(playerimg, (x, y))

# Función para dibujar al enemigo en la pantalla
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
    if distance < 27:
        return True
    else:
        return False

# Función para mostrar el texto game over en pantalla
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(over_text, text_rect)

# Función para mostrar el menú
def show_menu():
    menu_font = pygame.font.Font(asset_font, 32)
    instructions = [
        "Presiona 'J' para Jugar",
        "Presiona 'I' para Instrucciones",
        "Presiona 'V' para Ver Puntajes",
        "Presiona 'M' para Pausar Música",
        "Presiona 'R' para Reiniciar",
        "Presiona 'S' para Salir"
    ]
    for i, line in enumerate(instructions):
        text = menu_font.render(line, True, (255, 255, 255))
        screen.blit(text, (screen_width / 2 - 150, 200 + i * 40))

# Función principal del juego
def gameloop():
    global score
    global playerX
    global playerX_change
    global bulletX
    global bulletY
    global bullet_state
    global timer
    global game_speed
    global last_time
    global music_paused

    in_game = True
    while in_game:
        # Maneja eventos, actualiza y renderiza el juego
        # Limpia la pantalla
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Mostrar menú
        show_menu()

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
                if event.key == pygame.K_m:  # Pausar música
                    if music_paused:
                        pygame.mixer.music.unpause()
                        music_paused = False
                    else:
                        pygame.mixer.music.pause()
                        music_paused = True
                if event.key == pygame.K_j:  # Comenzar el juego
                    in_game = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Aquí se está actualizando la posición del jugador
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Bucle que se ejecuta para cada enemigo
        for i in range(no_of_enemies):
            if enemyY[i] > 400:
                for j in range(no_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -5
                enemyY[i] += enemyY_change[i]

            # Aquí se comprueba si ha habido una colisión entre el enemigo y la bala
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "Ready"
                score += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "Ready"

        if bullet_state == "Fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score()

        # Incrementar velocidad cada 10 segundos
        current_time = pygame.time.get_ticks()
        if current_time - last_time >= speed_increment_time:
            game_speed += 1
            last_time = current_time

        clock.tick(game_speed)
        pygame.display.update()

# Iniciar el bucle del juego
gameloop()
