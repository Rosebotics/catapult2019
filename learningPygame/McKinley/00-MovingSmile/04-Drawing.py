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

    # Draws the yellow head
    pygame.draw.circle(screen, (255,255,0), (300,300), 250)
    pygame.draw.circle(screen, (0, 0, 0), (300, 300), 250, 5)

    # draws the eyes
    pygame.draw.circle(screen, (0, 0, 0), (205, 200), 20)
    pygame.draw.circle(screen, (0, 0, 0), (400, 200), 20)

    # draws the nose
    pygame.draw.circle(screen, (255, 0, 0), (300, 300), 35)
    pygame.draw.circle(screen, (0, 0, 0), (300, 300), 35, 2)

    # draws the mouth
    pygame.draw.rect(screen, (127, 0, 0), (200, 400, 200, 25))

    # pygame.draw.rect(screen, color, (x, y, width, height), thickness)
    # pygame.draw.rect(screen, (100, 0, 0), (240, 350, 160, 30))


    pygame.display.update()
