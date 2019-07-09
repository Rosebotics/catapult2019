import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((480, 460))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#    screen.fill((255,0,0))
    screen.fill((0, 100, 100))
    pygame.display.update()