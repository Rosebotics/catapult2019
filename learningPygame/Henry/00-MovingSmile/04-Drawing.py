import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
#right = pygame.transform(screen, 45)
#left = pygame.transform(screen, -45)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#    screen.fill((255,0,0))
    screen.fill((40, 40, 40))
    pygame.draw.circle(screen, (190, 190, 0), (320, 240), 110)
    pygame.draw.circle(screen, (0, 0, 0), (280, 200), 10)
    pygame.draw.circle(screen, (0, 0, 0), (360, 200), 10)
    pygame.draw.circle(screen, (0, 0, 0), (320, 240), 8)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((300, 290), (40, 10)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((260, 290), (40, 10)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((340, 290), (40, 10)))
    pygame.display.update()
# TODO: In this module we'll start drawing a simple smiley face
#  Yellow circle for the head
#  Two black circle eyes
#  Red rectangle (rect) mouth
#  Red circle nose.