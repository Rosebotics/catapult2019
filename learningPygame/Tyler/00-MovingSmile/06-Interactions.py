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
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('cool smiley face')

eye_x = 0

nose_y = 230
clock = pygame.time.Clock()
noseR = 0
noseG = 0
noseB = 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            nose_y -= 30

        if pressed_keys[pygame.K_LEFT]:
            eye_x -= 5

        if pressed_keys[pygame.K_RIGHT]:
            eye_x += 5

        if pressed_keys[pygame.K_SPACE]:
            noseR += 5
            noseG += 10
            noseB += 15



    #screen.fill((255,0,0))
    #screen.fill((0, 255, 0))
    screen.fill((0, 100, 200))

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 150) #face
    pygame.draw.circle(screen, (0, 0, 0), (280 + eye_x, 170), 10) #eyes
    pygame.draw.circle(screen, (0, 0, 0), (366 + eye_x, 170), 10)

    nose_y = nose_y + 1
    pygame.draw.circle(screen, (noseR, noseG, noseB), (320, nose_y), 10) #nose
    if nose_y == 300:
        nose_y = 230

    pygame.draw.arc(screen, (0, 0 , 0), (270, 310, 100, 20), math.pi, 0, 5) #mouth
    #pygame.draw.rect(screen, (2, 0, 0), (320, 280, 20, 50), 5)

    pygame.display.update()