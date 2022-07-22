import pygame
import sys
import random
import colorsys
from math import *


# presets da tela
width = 500
heigth = 500

centerX = width/2
centerY = heigth/2

# Cor do plano de fundo
backgroundColor = (0, 0, 0)
black = (0, 0, 0)

# Tamanho da tela
screen = pygame.display.set_mode((width, heigth))

# PHYLLOTAXIS PRESETS
n = 1  # contador
c = 7  # determina a distancia entre as fileiras
angleDegree = 137.5


def drawCircle(angle, radius, color):
    # convertendo as coordenadas polares para cartesianas
    x = radius * cos(angle)+centerX
    y = radius * sin(angle)+centerY
    # retornado o circulo na coordenadas
    return pygame.draw.circle(screen, color, (x, y), 3)


def getAngle(angleDegree):
    return angleDegree/360*2*pi


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


# EXECUTANDO A TELA
while 1:
    screen.fill(black)
    # Verificando a saida do usuário
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Desenhando a PHYLLOTAXIS
    for i in range(n):
        angle = i * getAngle(angleDegree)
        radius = c * sqrt(i)

        color = (200, (radius*3) % 255, 100*angle % 255)

        drawCircle(angle, radius, color)

    pygame.display.update()

    # adicionando ao contador e colando um limite
    n += 2
    if n == 1000:
        n = 0
