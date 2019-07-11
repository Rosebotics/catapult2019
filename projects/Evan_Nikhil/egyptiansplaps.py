import pygame, sys, random, time
from pygame.locals import *








def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("this is a test")
    screen = pygame.display.set_mode((2000, 1000))
    #---------------set up---------------------------------------------------------------------------------------------------------









    while True:
        clock.tick(60)

        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == QUIT:
                sys.exit()
            #-----in for loop---------------------------------------------------------------------------------------------------



        #------------out of for loop-------------------------------------------------------------------------------
        screen.fill((220, 181, 121))















        pygame.display.update()

main()