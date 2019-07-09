# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.


import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
nose_y = 240
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 0, 255))  # magenta

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 150)
    pygame.draw.circle(screen, (0, 0, 0), (240, 160), 20)
    pygame.draw.circle(screen, (0, 0, 0), (400, 160), 20)
    nose_y = nose_y + 1
    if nose_y >480:
        nose_y = 240

    pygame.draw.circle(screen, (0, 20, 0), (320, nose_y), 10)
    pygame.draw.rect(screen, (255, 0, 0), (275, 270, 100, 50))#mouth

    pygame.display.update()