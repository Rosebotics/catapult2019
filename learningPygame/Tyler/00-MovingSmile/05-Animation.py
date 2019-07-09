# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.

import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))

nose_y = 230
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    #screen.fill((255,0,0))
    #screen.fill((0, 255, 0))
    screen.fill((0, 100, 200))

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 150) #face
    pygame.draw.circle(screen, (0, 0, 0), (280, 170), 10) #eyes
    pygame.draw.circle(screen, (0, 0, 0), (366, 170), 10)

    nose_y = nose_y + 1
    pygame.draw.circle(screen, (0, 0, 0), (320, nose_y), 10) #nose
    if nose_y == 300:
        nose_y = 230

    pygame.draw.arc(screen, (0, 0 , 0), (270, 310, 100, 20), math.pi, 0, 5) #mouth
    #pygame.draw.rect(screen, (2, 0, 0), (320, 280, 20, 50), 5)

    pygame.display.update()