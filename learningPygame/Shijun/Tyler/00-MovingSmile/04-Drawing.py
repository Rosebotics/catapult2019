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
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    #screen.fill((255,0,0))
    #screen.fill((0, 255, 0))
    screen.fill((60, 100, 0))

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 150)
    pygame.draw.circle(screen, (0, 0, 0), (280, 170), 10)
    pygame.draw.circle(screen, (0, 0, 0), (366, 170), 10)
    pygame.draw.arc(screen, (0, 0 , 0), (320, 310, 50, 50), 90, 180)


    pygame.display.update()