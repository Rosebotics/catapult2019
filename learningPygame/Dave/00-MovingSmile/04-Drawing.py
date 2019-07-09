# TODO: In this module we'll start drawing a simple smiley face
#  Yellow circle for the head
#  Two black circle eyes
#  Red rectangle (rect) mouth
#  Red circle nose.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((120, 80, 0))  # Brown

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 210)
    pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)

    pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)
    pygame.draw.circle(screen, (0, 0, 0), (242, 162), 7)

    pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)
    pygame.draw.circle(screen, (0, 0, 0), (398, 162), 7)

    pygame.draw.circle(screen, (80, 0, 0), (320, 240), 15, 6)

    pygame.display.update()
