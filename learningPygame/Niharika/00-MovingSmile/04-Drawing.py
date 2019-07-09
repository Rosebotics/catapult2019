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
    screen.fill((0, 255, 255))  #Cyan

    pygame.draw.circle(screen, (255,255,0), (320,240), 150) # face
    pygame.draw.circle(screen, (0, 0, 0), (270, 200), 20) #left eye
    pygame.draw.circle(screen, (0, 0, 0), (370, 200), 20) #right eye
    pygame.draw.circle(screen, (165, 42, 42), (370, 200), 35, 1)# right lens
    pygame.draw.circle(screen, (165, 42, 42), (270, 200), 35, 1) #left lens
    pygame.draw.line(screen, (165, 42, 42), (305,200), (335, 200), 1) #glasses center
    pygame.draw.line(screen, (165, 42, 42), (250, 175), (200, 160), 1)  # left glasses lever
    pygame.draw.line(screen, (165, 42, 42), (395, 175), (445, 160), 1)  # right glasses lever

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 275, 120, 50))#tongue
    pygame.draw.ellipse(screen, (255,0,0), pygame.Rect(300,285, 50, 60))#tongue
    pygame.draw.line(screen, (0,0,0), (325,290), (325,325), 2)#tongue


    pygame.draw.circle(screen, (0, 0, 0), (325, 250), 10)  # nose

    pygame.display.update()