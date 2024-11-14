import pygame
import random
import sys

# Inicialización de Pygame y el controlador
pygame.init()
pygame.joystick.init()

# Configuración de la pantalla
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Blocks Space")

# Colores
COLOR_FONDO = (30, 30, 30)
COLOR_JUGADOR = (0, 128, 255)
COLOR_OBSTACULO = (255, 0, 0)
COLOR_TEXTO = (255, 255, 255)

# Fuentes
fuente = pygame.font.Font(None, 36)

# Jugador
jugador_tamaño = 50
jugador_pos = [ANCHO // 2, ALTO - 2 * jugador_tamaño]

# Obstáculos
obstaculo_tamaño = 50
obstaculo_pos = [random.randint(0, ANCHO - obstaculo_tamaño), 0]
obstaculo_velocidad = 10

# Puntaje
puntaje = 0

# Reloj
reloj = pygame.time.Clock()

# Función para detectar colisiones
def detectar_colision(jugador_pos, obstaculo_pos):
    jx, jy = jugador_pos
    ox, oy = obstaculo_pos
    if (ox < jx < ox + obstaculo_tamaño or ox < jx + jugador_tamaño < ox + obstaculo_tamaño) and \
       (oy < jy < oy + obstaculo_tamaño or oy < jy + jugador_tamaño < oy + obstaculo_tamaño):
        return True
    return False

# Función para mostrar el puntaje
def mostrar_puntaje(puntaje):
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, COLOR_TEXTO)
    pantalla.blit(texto_puntaje, (10, 10))

# Bucle principal del juego
def juego():
    global jugador_pos, obstaculo_pos, obstaculo_velocidad, puntaje
    juego_activo = True

    # Inicialización del joystick
    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

    # Bucle principal del juego
    while juego_activo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento del jugador (teclado o mando)
        teclas = pygame.key.get_pressed()

        if joystick:  # Usar el joystick del mando
            eje_x = joystick.get_axis(0)  # Obtener el movimiento horizontal del joystick
            if eje_x < -0.1 and jugador_pos[0] > 0:
                jugador_pos[0] -= 10
            if eje_x > 0.1 and jugador_pos[0] < ANCHO - jugador_tamaño:
                jugador_pos[0] += 10
        else:  # Usar teclado
            if teclas[pygame.K_LEFT] and jugador_pos[0] > 0:
                jugador_pos[0] -= 10
            if teclas[pygame.K_RIGHT] and jugador_pos[0] < ANCHO - jugador_tamaño:
                jugador_pos[0] += 10

        # Movimiento del obstáculo
        obstaculo_pos[1] += obstaculo_velocidad
        if obstaculo_pos[1] > ALTO:
            # Si el obstáculo salió de la pantalla, se incrementa el puntaje
            puntaje += 1
            obstaculo_pos = [random.randint(0, ANCHO - obstaculo_tamaño), 0]

            # Incrementar la velocidad de caída de los bloques cada 5 puntos
            if puntaje % 5 == 0:
                obstaculo_velocidad += 1

        # Comprobar colisión
        if detectar_colision(jugador_pos, obstaculo_pos):
            juego_activo = False

        # Dibujar elementos en la pantalla
        pantalla.fill(COLOR_FONDO)
        pygame.draw.rect(pantalla, COLOR_JUGADOR, (*jugador_pos, jugador_tamaño, jugador_tamaño))
        pygame.draw.rect(pantalla, COLOR_OBSTACULO, (*obstaculo_pos, obstaculo_tamaño, obstaculo_tamaño))

        # Mostrar el puntaje
        mostrar_puntaje(puntaje)

        # Actualizar pantalla
        pygame.display.flip()

        # Velocidad del juego
        reloj.tick(30)

# Llamar directamente al juego
juego()
