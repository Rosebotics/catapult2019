# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.


# TODO: In this module we'll start drawing a simple smiley face
#  Yellow circle for the head
#  Two black circle eyes
#  Red rectangle (rect) mouth
#  Red circle nose.

import pygame
import sys
pygame.init()   # initializes pygame, necessary to use
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 255, 255))
    pygame.draw.circle(screen, (255, 255, 0), (320, 240), 150, 0)
    pygame.draw.circle(screen, (0, 0, 0), (250, 200), 25, 0)
    pygame.draw.circle(screen, (0, 0, 0), (390, 200), 25, 0)
    pygame.draw.circle(screen, (0, 0, 0), (320, 275), 10, 0)
    # pygame.draw.rect(screen, (255, 0, 0),)
    pygame.display.update()
