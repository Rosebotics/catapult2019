# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

nose_y=250
clock=pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 80, 80))

    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 200)
    pygame.draw.circle(screen, (0, 0, 0), (250, 200), 40)
    pygame.draw.circle(screen, (0, 0, 0), (390, 200), 40)
    pygame.draw.rect(screen, (0, 0, 0), (270, 340, 100, -50), 30)
    pygame.draw.line(screen, (255, 255, 0), (250, 280), (390, 280), 49)
    pygame.draw.circle(screen, (0, 0, 0), (320, nose_y), 20)

    nose_y =nose_y + 1
    if nose_y > 420:
        nose_y = 250


    pygame.display.update()