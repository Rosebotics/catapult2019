# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
#right = pygame.transform(screen, 45)
#left = pygame.transform(screen, -45)
noseY = 240
leftEyeX = 280
rightEyeX = 360
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        noseY = 240

    if noseY > 480:
        noseY = 240
    else:
        noseY += 2
    if pressed_keys[pygame.K_RIGHT]:
        rightEyeX += 1
        leftEyeX += 1
    else:
        if pressed_keys[pygame.K_LEFT]:
            rightEyeX -= 1
            leftEyeX -= 1

    screen.fill((40, 40, 40))
    pygame.draw.circle(screen, (190, 190, 0), (320, 240), 110)
    pygame.draw.circle(screen, (0, 0, 0), (leftEyeX, 200), 10)
    pygame.draw.circle(screen, (0, 0, 0), (rightEyeX, 200), 10)
    pygame.draw.circle(screen, (0, 0, 0), (320, noseY), 8)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((300, 290), (40, 10)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((260, 290), (40, 10)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((340, 290), (40, 10)))

    pygame.display.update()
# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.