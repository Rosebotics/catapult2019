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

nose_y = 254
eye_x = 247
eyes_x = 380
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            nose_y = 50
    screen.fill((150,0,250)) # purple
    pygame.draw.circle(screen,(200,200,0), (320,240), 150)

    eye_x = eye_x + 1
    if eye_x > 440:
        eye_x = 340
    pygame.draw.circle(screen, (0,0,0), (eye_x, 200), (20))

    eyes_x = eyes_x + 1
    if eyes_x > 270:
        eyes_x = 200
    pygame.draw.circle(screen, (0,0,0), (eyes_x,200), (20))

    nose_y = nose_y+2
    if nose_y > 480:
        nose_y = 254
    pygame.draw.circle(screen, (200,0,0), (315, nose_y), (15), (5))

    pygame.draw.rect(screen, (150,0,0), (283, 298, 70, 30))
    pygame.draw.circle(screen, (200, 0, 0), (400,265), (20))
    pygame.draw.circle(screen, (200, 0, 0), (231,265), (20))
    pygame.display.update()