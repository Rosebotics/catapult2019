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
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(     (255, 0, 0)     ) # Red
    # screen.fill(     (0, 255, 0)     ) # Green
    # screen.fill(     (255, 255, 0)     ) # YellowX
    # screen.fill(      (0, 255, 255)       ) # Cyan
    # screen.fill(    (150, 120, 0)     ) # Brown
    # screen.fill(   (255, 0, 255)    ) # Magenta
    pygame.draw.circle(screen, (225, 225, 0), (320, 240), 150)
    pygame.draw.circle(screen, (0, 0, 0), (260, 200), 10, 5)
    pygame.draw.circle(screen, (0, 0, 0), (380, 200), 10, 5)

    pygame.display.update()





