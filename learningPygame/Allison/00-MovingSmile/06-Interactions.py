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
pygame.init()   # initializes pygame, necessary to use
screen = pygame.display.set_mode((640, 480))
nosey = 275
clock = pygame.time.Clock()
factor = 4
eyes = 0
while True:
    clock.tick(60)
    pygame.display.set_caption('Moving Smiley Face')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[pygame.K_UP]:
            factor -= 2
        if pressedkeys[pygame.K_DOWN]:
            factor += 2
        if pressedkeys[pygame.K_LEFT]:
            eyes -= 3
        if pressedkeys[pygame.K_RIGHT]:
             eyes += 3
    screen.fill((0, 255, 255))
    face = pygame.draw.circle(screen, (255, 255, 0), (320, 240), 150, 0)
    lefteye = pygame.draw.circle(screen, (0, 0, 0), (250 + eyes, 200), 25, 0)
    righteye = pygame.draw.circle(screen, (0, 0, 0), (390 + eyes, 200), 25, 0)
    nose = pygame.draw.circle(screen, (255, 0, 0), (320, nosey), 10, 0)
    nosey += factor
    if nosey > 480 or nosey < 0:
        nosey = 275
    mouth = pygame.draw.rect(screen, (255, 0, 0), (270, 350, 100, 10), 0)
    pygame.display.update()
