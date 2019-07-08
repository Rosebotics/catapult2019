# TODO: In this module we'll add color to the window.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 0, 255)) # red
    screen.fill((0, 255, 0)) # green
    screen.fill((255, 255, 0)) # yellow
    screen.fill((51, 255, 255)) # cyan
    screen.fill((153, 76, 0)) # brown
    screen.fill((255, 0, 255)) # magenta
    pygame.display.update()