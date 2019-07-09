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

    nose_y = nose_y + 2
    if nose_y > 480:
        nose_y = 240
    pygame.draw.circle(screen, (80, 0, 0), (320, nose_y), 15, 6)

    # pygame.draw.rect(screen, color, (x, y, width, height), thickness)
    pygame.draw.rect(screen, (100, 0, 0), (220, 350, 200, 30))

    pygame.display.update()
