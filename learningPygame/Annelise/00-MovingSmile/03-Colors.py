# Done: Copy all of your   02-TheGameLoop.py   program and put it below this comment.


# TODO    One way to do so is:
# TODO      1. Inside  02-TheGameLoop.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        # print(event) - shows every event that occurs while this is here
        if event.type == pygame.QUIT:
            sys.exit()
    # screen.fill(  (255, 0, 0)  ) #RED
    # screen.fill(  (0, 255, 0)  ) #GREEN
    # screen.fill(  (255, 255, 0))   #YELLOW
    # screen.fill(  (0,0,255)  ) #BLUE
    # screen.fill(  (255, 0, 225)  ) #MAGENTA
    # screen.fill(  (90, 30, 20)  ) #BROWN
    # screen.fill(  (0, 255, 255)  ) #CYAN
    pygame.display.update()

# TODO: In this module we'll add color to the window