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

    screen.fill((255, 0, 255)) # magenta

    pygame.draw.circle(screen, (200,200,0), (320,240), 150)
    pygame.draw.circle(screen, (255, 255, 255), (240, 160), 20)
    pygame.draw.circle(screen, (255, 255, 255), (400, 160), 20)
    pygame.draw.circle(screen, (255, 255, 255), (320, 240), 10)
    pygame.draw.circle(screen, (255, 255, 255), (220, 300), 20)
    pygame.draw.circle(screen, (255, 255, 255), (240, 320), 20)
    pygame.draw.circle(screen, (255, 255, 255), (260, 340), 20)
    pygame.draw.circle(screen, (255, 255, 255), (270, 350), 20)
    pygame.draw.circle(screen, (255, 255, 255), (288, 355), 20)
    pygame.draw.circle(screen, (255, 255, 255), (310, 362), 20)
    pygame.draw.circle(screen, (255, 255, 255), (270, 350), 20)
    pygame.draw.circle(screen, (255, 255, 255), (270, 350), 20)
    pygame.draw.circle(screen, (255, 255, 255), (270, 350), 20)
    pygame.draw.circle(screen, (255, 255, 255), (270, 350), 20)
    pygame.draw.circle(screen, (255, 255, 255), (270, 350), 20)
    pygame.draw.circle(screen, (255, 255, 255), (270, 350), 20)
    pygame.draw.circle(screen, (255, 255, 255), (270, 350), 20)

    pygame.display.update()