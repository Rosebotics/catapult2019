# TODO: Copy all of your   05-Animation.py   program and put it below this comment.

# TODO: In this module we'll make the nose reset when the up arrow is pressed.
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("this is the end of the world")
nose_y = 0
eyes_y = 0
leye_x = 0
reye_x = 0
crad = 0
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pressed_keys[pygame.K_w]:
            crad += 10
            if crad > 150:
                crad = 150
        if pressed_keys[pygame.K_s]:
            crad -= 10
            if crad < -150:
                crad = -150

    if pressed_keys[pygame.K_UP]:
       # nose_y = -50
        eyes_y -= 10
    if pressed_keys[pygame.K_LEFT]:
        leye_x -= 10
        reye_x += 10
    if pressed_keys[pygame.K_RIGHT]:
        leye_x += 10
        reye_x -= 10
    if pressed_keys[pygame.K_DOWN]:
        eyes_y += 10

    screen.fill((0, 255, 255))#teel

    # face
    pygame.draw.circle(screen, (255, 200, 100), (320, 240), 150+crad, 0)

   #eyes
    #eyes_y = eyes_y -1
   # if eyes_y < 10:
       # eyes_y = 180
    pygame.draw.circle(screen, (0, 0, 0), (245+leye_x, 180+eyes_y), 25, 0)
    pygame.draw.circle(screen, (0, 0, 0), (395+reye_x, 180+eyes_y), 25, 0)

   #nose
    nose_y = nose_y + 1
    if nose_y > 240:
        nose_y = -240
    pygame.draw.circle(screen, (255, 0, 0), (320, 240+nose_y), 15, 0)

    # squair mouth rect(screen, collor, (start),(with lange)
    #pygame.draw.rect(screen, (255, 250, 250), ((245, 290), (150, 30)), 0)

    # tryangel mouth
    pygame.draw.polygon(screen,(255,100,20),((350,280),(250,280),(300,300)))

    pygame.display.update()
# Additional challenges (time permitting):
#   Make the eyes move left and right with the left and right arrow button.
#   Make the nose color change when the spacebar is pressed.
#   Make the face grow and shrink with the g and s buttons.
#   Draw a proportionally incorrect stick figure body under the face using lines.
#   Make everything drawn move down off the screen if a the mouse down event occurs.
