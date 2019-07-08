
# TODO: In this module we'll add color to the window

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 0, 0)) #Red
    screen.fill((0, 255 , 0))#Green
    screen.fill((255, 255, 0))#Yellow
    screen.fill((0, 255, 255))  #Cyan
    screen.fill((150,130,0))#Brown
    screen.fill((255,0,255)) #Magenta



    pygame.display.update()