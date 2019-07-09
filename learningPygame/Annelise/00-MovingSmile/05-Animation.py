# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.

import pygame
import sys

nose_y = 240
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    clock.tick(60)
    for event in pygame.event.get():
        # print(event) - shows every event that occurs while this is here
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 255))

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 150)  # face

    # to make "unfilled" shapes, change the width of the shape and it will look unfilled or like a line
    pygame.draw.circle(screen, (0, 0, 0), (250, 200), 30)  # left eye
    pygame.draw.circle(screen, (0, 0, 0), (400, 200), 30)  # right eye

    # pygame.draw.rect(screen,   color,(x, y, width, height), thickness)
    pygame.draw.rect(screen, (255, 0, 0), (280, 300, 70, 40)) # mouth

    pygame.draw.circle(screen, (0, 0, 255), (250, 200), 12) #left iris
    pygame.draw.circle(screen, (0, 0, 255), (400, 200), 12) # right iris

    nose_y = nose_y + 1
    if nose_y > 480:
        nose_y = 240
    pygame.draw.circle(screen, (255, 0, 0), (320, nose_y), 15) # nose

    pygame.display.update()