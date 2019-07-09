# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

nose_y = 240
eyes_y = 180

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 255, 255))#teel

    # face
    pygame.draw.circle(screen, (255, 200, 100), (320, 240), 150, 0)

   #eyes
    #eyes_y = eyes_y -1
    if eyes_y < 10:
        eyes_y = 180
    pygame.draw.circle(screen, (0, 0, 0), (245, eyes_y), 25, 0)
    pygame.draw.circle(screen, (0, 0, 0), (395, eyes_y), 25, 0)

   #nose
    nose_y = nose_y + 1
    if nose_y > 480:
        nose_y = 240
    pygame.draw.circle(screen, (255, 0, 0), (320, nose_y), 15, 0)

    # squair mouth rect(screen, collor, (start),(with lange)
    #pygame.draw.rect(screen, (255, 250, 250), ((245, 290), (150, 30)), 0)

    # tryangel mouth
    pygame.draw.polygon(screen,(255,100,20),((350,280),(250,280),(300,300)))

    pygame.display.update()
# TODO: In this module we'll make the nose move down until a certain y then reset to the top again.