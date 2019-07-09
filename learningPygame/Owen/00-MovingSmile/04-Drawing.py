# TODO: In this module we'll start drawing a simple smiley face
#  Yellow circle for the head
#  Two black circle eyes
#  Red rectangle (rect) mouth
#  Red circle nose.
#07/08/2019

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 0, 255)) # magenta

    pygame.draw.circle(screen, (200,200,0), (320,240), 150)
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 20)
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 20)
    pygame.draw.circle(screen, (0, 20, 0), (320, 240), 10)
    pygame.draw.rect(screen, (255, 0, 0), (275, 270, 100, 50))

    pygame.display.update()