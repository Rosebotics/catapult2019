# TODO: Copy all of your   05-Animation.py   program and put it below this comment.

# TODO: In this module we'll make the nose reset when the up arrow is pressed.

# Additional challenges (time permitting):
#   Make the eyes move left and right with the left and right arrow button.
#   Make the nose color change when the spacebar is pressed.
#   Make the face grow and shrink with the g and s buttons.
#   Draw a proportionally incorrect stick figure body under the face using lines.
#   Make everything drawn move down off the screen if a the mouse down event occurs.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

nose_y=250
eye_ax=250
eye_bx=390
clock=pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            nose_y=60
        if pressed_keys[pygame.K_RIGHT]:
            eye_ax=280
        if pressed_keys[pygame.K_LEFT]:
            eye_ax=220
        if pressed_keys[pygame.K_RIGHT]:
            eye_bx=420
        if pressed_keys[pygame.K_LEFT]:
            eye_bx = 360
    screen.fill((255, 80, 80))

    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 200)
    pygame.draw.circle(screen, (0, 0, 0), (250, 200), 40)
    pygame.draw.circle(screen, (0, 0, 0), (390, 200), 40)
    pygame.draw.circle(screen, (255, 255, 255), (eye_ax, 200), 10)
    pygame.draw.circle(screen, (255, 255, 255), (eye_bx, 200), 10)
    pygame.draw.rect(screen, (0, 0, 0), (270, 340, 100, -50), 30)
    pygame.draw.line(screen, (255, 255, 0), (250, 280), (390, 280), 49)
    pygame.draw.circle(screen, (0, 0, 0), (320, nose_y), 20)

    nose_y =nose_y + 1
    if nose_y > 420:
        nose_y = 250


    pygame.display.update()