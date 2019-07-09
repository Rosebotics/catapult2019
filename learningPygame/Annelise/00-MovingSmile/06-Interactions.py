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

nose_y = 240
left_iris = 250
right_iris = 400
mouth_height = 40
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    clock.tick(60)
    for event in pygame.event.get():
        # print(event) - shows every event that occurs while this is here
        if event.type == pygame.QUIT:
            sys.exit()
# changes
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        nose_y = 50
    if pressed_keys[pygame.K_LEFT]:
        left_iris = left_iris - 5
        right_iris = right_iris - 5
    if pressed_keys[pygame.K_RIGHT]:
        left_iris = left_iris + 5
        right_iris = right_iris + 5
    if pressed_keys[pygame.K_DOWN]:
        left_iris = 250
        right_iris = 400
    if pressed_keys[pygame.K_DOWN]:
        mouth_height = mouth_height - 5
        if mouth_height == 0:
            mouth_height = 40


    screen.fill((0, 0, 255))

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 150)  # face

    # to make "unfilled" shapes, change the width of the shape and it will look unfilled or like a line
    pygame.draw.circle(screen, (0, 0, 0), (250, 200), 30)  # left eye
    pygame.draw.circle(screen, (0, 0, 0), (400, 200), 30)  # right eye

    # pygame.draw.rect(screen,   color,(x, y, width, height), thickness)
    pygame.draw.rect(screen, (255, 0, 0), (280, 300, 80, mouth_height)) # mouth

    pygame.draw.circle(screen, (0, 0, 255), (left_iris, 200), 12) #left iris
    pygame.draw.circle(screen, (0, 0, 255), (right_iris, 200), 12) # right iris

    nose_y = nose_y + 1
    if nose_y > 480:
        nose_y = 240
    pygame.draw.circle(screen, (255, 0, 0), (320, nose_y), 15) # nose

    pygame.display.update()