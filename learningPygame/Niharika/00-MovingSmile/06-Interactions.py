# TODO: Copy all of your   05-Animation.py   program and put it below this comment.

# TODO: In this module we'll make the nose reset when the up arrow is pressed.

# Additional challenges (time permitting):
#   Make the eyes move left and right with the left and right arrow button.
#   Make the nose color change when the spacebar is pressed.
#   Make the face grow and shrink with the g and s buttons.
#   Draw a proportionally incorrect stick figure body under the face using lines.
#   Make everything drawn move down off the screen if a the mouse down event occurs.

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

lefteye_x = 270
righteye_x = 370
rightlens_x =370
leftlens_x = 270
nose_y = 250
tongue_y = 60
glassescenter_startx = 305
glassescenter_endx = 335
leftglass_endlever_x = 200
rightglass_endlever_x = 445
clock = pygame.time.Clock()

while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        nose_y =50
    if pressed_keys[pygame.K_RIGHT]:
        righteye_x =righteye_x + 5
        lefteye_x = lefteye_x + 5
        leftlens_x = leftlens_x +5
        rightlens_x = rightlens_x + 5
        glassescenter_startx = glassescenter_startx +5
        glassescenter_endx = glassescenter_endx +5
        #leftglass_endlever_x = leftglass_endlever_x +5
        #rightglass_endlever_x = rightglass_endlever_x +5
    if pressed_keys[pygame.K_LEFT]:
        lefteye_x = lefteye_x - 5
        righteye_x = righteye_x - 5
        leftlens_x = leftlens_x - 5
        rightlens_x = rightlens_x - 5
        glassescenter_startx = glassescenter_startx -5
        glassescenter_endx = glassescenter_endx -5
        #rightglass_endlever_x = rightglass_endlever_x -5
        #leftglass_endlever_x = leftglass_endlever_x -5
    if pressed_keys[pygame.K_DOWN]:
        tongue_y = tongue_y + 5





    screen.fill((0, 255, 255))  #Cyan

    pygame.draw.circle(screen, (255,255,0), (320,240), 150) # face
    pygame.draw.circle(screen, (0, 0, 0), (lefteye_x, 200), 20) #left eye
    pygame.draw.circle(screen, (0, 0, 0), (righteye_x, 200), 20) #right eye
    pygame.draw.circle(screen, (165, 42, 42), (rightlens_x, 200), 35, 1)# right lens
    pygame.draw.circle(screen, (165, 42, 42), (leftlens_x, 200), 35, 1) #left lens
    pygame.draw.line(screen, (165, 42, 42), (glassescenter_startx,200), (glassescenter_endx, 200), 1) #glasses center
    pygame.draw.line(screen, (165, 42, 42),(250, 175), (leftglass_endlever_x, 160),1) #left glasses lever
    pygame.draw.line(screen, (165, 42, 42),(395,175), (rightglass_endlever_x, 160),1)# right glasses lever

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 275, 120, 50))#mouth
    pygame.draw.ellipse(screen, (255,0,0), pygame.Rect(300,285, 50, tongue_y))#tongue
    pygame.draw.line(screen, (0,0,0), (325,290), (325,325), 2)#tongue

    nose_y = nose_y + 2
    if nose_y > 480:
        nose_y = 250
    pygame.draw.circle(screen, (0, 0, 0), (325, nose_y), 10)  # nose

    pygame.display.update()