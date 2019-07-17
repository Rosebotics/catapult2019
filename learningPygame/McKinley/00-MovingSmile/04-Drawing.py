# TODO: In this module we'll start drawing a simple smiley face
#  Yellow circle for the head
#  Two black circle eyes
#  Red rectangle (rect) mouth
#  Red circle nose.

import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((600, 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 200, 200))


    pygame.draw.circle(screen, (255,255,0), (300,300), 250)
    pygame.draw.circle(screen, (0, 0, 0), (300, 300), 250, 5)

    pygame.draw.circle(screen, (0, 0, 0), (225, 200), 20)
    pygame.draw.circle(screen, (0, 0, 0), (375, 200), 20)

    pygame.display.update()