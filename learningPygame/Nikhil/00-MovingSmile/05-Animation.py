# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
nose_y = 240

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(     (255, 0, 0)     ) # Red
    # screen.fill(     (0, 255, 0)     ) # Green
    # screen.fill(     (255, 255, 0)     ) # YellowX
    # screen.fill(      (0, 255, 255)       ) # Cyan
    # screen.fill(    (150, 120, 0)     ) # Brown
    # screen.fill(   (255, 0, 255)    ) # Magenta
    pygame.draw.circle(screen, (225, 225, 0), (320, 240), 150)
    pygame.draw.circle(screen, (0, 0, 0), (260, 200), 10, 5)
    pygame.draw.circle(screen, (0, 0, 0), (380, 200), 10, 5)
    nose_y = nose_y + 2
    if nose_y > 480:
        nose_y = 240
    pygame.draw.circle(screen, (0, 0, 0), (324, nose_y), 10, 5)
    pygame.draw.rect(screen, (0, 0, 0), (260, 310, 120, 50))
    pygame.display.update()