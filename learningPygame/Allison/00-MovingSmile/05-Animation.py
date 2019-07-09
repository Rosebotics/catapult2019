# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.
import pygame
import sys
pygame.init()   # initializes pygame, necessary to use
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
nosey = 275
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 255, 255))
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 150, 0)
    pygame.draw.circle(screen, (0, 0, 0), (250, 200), 25, 0)
    pygame.draw.circle(screen, (0, 0, 0), (390, 200), 25, 0)
    pygame.draw.circle(screen, (255, 0, 0), (320, nosey), 10, 0)
    nosey += 1
    if nosey > 480:
        nosey = 275
    mouth = pygame.draw.rect(screen, (255, 0, 0), (270, 350, 100, 10), 0)
    pygame.display.update()
