# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

nose_y = 254
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((150,0,250)) # purple
    pygame.draw.circle(screen,(200,200,0), (320,240), 150)
    pygame.draw.circle(screen, (0,0,0), (247,200), (20))
    pygame.draw.circle(screen, (0,0,0), (380, 200), (20))

    nose_y = nose_y+2
    if nose_y > 480:
        nose_y = 254
    pygame.draw.circle(screen, (200,0,0), (315, nose_y), (15), (5))

    pygame.draw.rect(screen, (150,0,0), (283, 298, 70, 30))
    pygame.draw.circle(screen, (200, 0, 0), (400,265), (20))
    pygame.draw.circle(screen, (200, 0, 0), (231,265), (20))
    pygame.display.update()