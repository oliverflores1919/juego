import pygame
import random
import sys


pygame.init()


ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los obstáculos")


COLOR_FONDO = (30, 30, 30)
COLOR_JUGADOR = (0, 128, 255)
COLOR_OBSTACULO = (255, 0, 0)


jugador_tamaño = 50
jugador_pos = [ANCHO // 2, ALTO - 2 * jugador_tamaño]


obstaculo_tamaño = 50
obstaculo_pos = [random.randint(0, ANCHO - obstaculo_tamaño), 0]
obstaculo_velocidad = 35


reloj = pygame.time.Clock()


def detectar_colision(jugador_pos, obstaculo_pos):
    jx, jy = jugador_pos
    ox, oy = obstaculo_pos

    if (ox < jx < ox + obstaculo_tamaño or ox < jx + jugador_tamaño < ox + obstaculo_tamaño) and \
       (oy < jy < oy + obstaculo_tamaño or oy < jy + jugador_tamaño < oy + obstaculo_tamaño):
        return True
    return False


juego_activo = True
while juego_activo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_pos[0] > 0:
        jugador_pos[0] -= 15
    if teclas[pygame.K_RIGHT] and jugador_pos[0] < ANCHO - jugador_tamaño:
        jugador_pos[0] += 15

    
    obstaculo_pos[1] += obstaculo_velocidad
    if obstaculo_pos[1] > ALTO:
        obstaculo_pos = [random.randint(0, ANCHO - obstaculo_tamaño), 0]

    
    if detectar_colision(jugador_pos, obstaculo_pos):
        juego_activo = False

    
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_JUGADOR, (*jugador_pos, jugador_tamaño, jugador_tamaño))
    pygame.draw.rect(pantalla, COLOR_OBSTACULO, (*obstaculo_pos, obstaculo_tamaño, obstaculo_tamaño))

    
    pygame.display.flip()

    
    reloj.tick(30)


pygame.quit()
