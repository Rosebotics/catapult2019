

# TODO: In this module we'll add color to the window

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #screen.fill((255,0,0))
    #screen.fill((0, 255, 0))
    screen.fill((60, 30, 0))

    pygame.display.update()
