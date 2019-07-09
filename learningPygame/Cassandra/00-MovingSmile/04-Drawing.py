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

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((150,0,250)) # purple
    pygame.draw.circle(screen,(200,200,0), (320,240), 150)
    pygame.draw.circle(screen, (0,0,0), (247,200), (20))
    pygame.draw.circle(screen, (0,0,0), (380, 200), (20))
    pygame.draw.circle(screen, (200,0,0), (315, 254), (15), (5))
    pygame.draw.rect(screen, (150,0,0), (283, 298, 70, 30))
    pygame.draw.circle(screen, (200, 0, 0), (392,265), (20))
    pygame.draw.circle(screen, (200, 0, 0), (231,265), (20))
    pygame.display.update()