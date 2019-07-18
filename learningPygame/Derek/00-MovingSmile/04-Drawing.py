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
import math

pygame.init()

running = True

frame = pygame.display.set_mode((640, 480))

red_value = 255
circle_radius = 25

screen_red = 0
screen_green = 0
screen_blue = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame.fill((screen_red, screen_green, screen_blue))

    screen_red += 1

    if screen_red > 255:
        screen_red = 0

    screen_green += 1

    if screen_green > 255:
        screen_green = 0

    screen_blue += 1

    if screen_blue > 255:
        screen_blue = 0

    red_value -= 1

    if red_value < 0:
        red_value = 255

    circle_radius -= 1

    if circle_radius < 0:
        circle_radius = 25

    face = pygame.draw.circle(frame, (255, 255, 255), (320, 240), 140)

    left_eye = pygame.draw.circle(frame, (red_value, 0, 0), (260, 200), circle_radius)

    right_eye = pygame.draw.circle(frame, (red_value, 0, 0), (380, 200), circle_radius)

    nose = pygame.draw.circle(frame, (255, 0, 255), (320, 240), circle_radius)

    mouth = pygame.draw.arc(frame, (red_value, 0, 0), (270, 260, 100, 100), math.pi, 2*math.pi, 10)

    pygame.display.update()