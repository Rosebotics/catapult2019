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
clock = pygame.time.Clock()
nose_y = 240
left_eye_x = 260
right_eye_x = 380

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] :
            nose_y = 50

        if pressed_keys[pygame.K_LEFT] :
            left_eye_x -= 50

        if pressed_keys[pygame.K_RIGHT] :
            left_eye_x += 50




    screen.fill(     (255, 0, 0)     ) # Red
    # screen.fill(     (0, 255, 0)     ) # Green
    # screen.fill(     (255, 255, 0)     ) # YellowX
    # screen.fill(      (0, 255, 255)       ) # Cyan
    # screen.fill(    (150, 120, 0)     ) # Brown
    # screen.fill(   (255, 0, 255)    ) # Magenta
    pygame.draw.circle(screen, (225, 225, 0), (320, 240), 150)
    pygame.draw.circle(screen, (0, 0, 0), (left_eye_x, 200), 10, 5)
    right_eye = pygame.draw.circle(screen, (0, 0, 0), (right_eye_x, 200), 10, 5)
    nose_y = nose_y + 2
    if nose_y > 480:
        nose_y = 240
    pygame.draw.circle(screen, (0, 0, 0), (324, nose_y), 10, 5)
    pygame.draw.rect(screen, (0, 0, 0), (260, 310, 120, 50))
    pygame.display.update()