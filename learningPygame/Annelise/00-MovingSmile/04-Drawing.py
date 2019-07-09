# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

# change
# TODO: In this module we'll start drawing a simple smiley face
#  Yellow circle for the head
#  Two black circle eyes
#  Red rectangle (rect) mouth
#  Red circle nose.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        # print(event) - shows every event that occurs while this is here
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 255))

    pygame.draw.circle(screen, (200, 200, 0), (320, 240), 150) # face
    pygame.draw.circle(screen, (0,0,0), (250, 200), 30) # left eye
    pygame.draw.circle(screen, (0,0,0), (400, 200), 30) # right eye
    # pygame.draw.circle(screen, (255,0,0), (320, 320), 40) # circle mouth
    # pygame.draw.rect(screen, color, (x, y, width, height), thickness)
    pygame.draw.rect(screen, (255, 0, 0), (280, 300, 70, 40)) # mouth
    pygame.draw.circle(screen, (0, 0, 255), (250, 200), 12) #left iris
    pygame.draw.circle(screen, (0, 0, 255), (400, 200), 12) # right iris
    pygame.draw.circle(screen, (255, 0, 0), (320, 250), 15) # nose

# http://blog.tankorsmash.com/?p=128 -- work on rotated rectangle mouth
    # bigger = pygame.Rect(0, 0, 100, 50)
    # smaller = pygame.Rect

    pygame.display.update()