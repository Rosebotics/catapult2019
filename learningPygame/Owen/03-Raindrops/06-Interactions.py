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
nose_y = 240
eye_x = 0
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            nose_y = 50
        if pressed_keys[pygame.K_LEFT]:
            eye_x = eye_x - 10
            if eye_x < 0:
                eye_x = 240

    screen.fill((255, 0, 255))  # magenta

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 150)
    pygame.draw.circle(screen, (0, 0, 0), (240 + eye_x, 160), 20)
    pygame.draw.circle(screen, (0, 0, 0), (400 + eye_x, 160), 20)
    nose_y = nose_y + 2
    if nose_y >480:
        nose_y = 240

    pygame.draw.circle(screen, (0, 20, 0), (320, nose_y), 10)
    pygame.draw.rect(screen, (255, 0, 0), (275, 270, 100, 50))#mouth

    pygame.display.update()