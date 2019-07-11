import pygame, sys, random, time
from pygame.locals import *

#-----------------------------------------------------------------------------Player
class Player:
    def __init__(self):
        pass

    def place_card(self):
        pass

    def slap(self):
        pass

    def draw(self):
        pass

#---------------------------------------------------------------------------------------CenterPile
class CenterPile:
    def __init__(self):
        pass

    def draw(self):
        pass

#-----------------------------------------------------------------------------------Detection
class Detection:
    def __init__(self):
        pass

    def slap(self):
        pass

    def win(self):
        pass

    def new_round(self):
        pass

#-------------------------------------------------------------------------------Challenge
class Challenge:
    def __init__(self):
        pass

#detect to set up tries remaining
    def card_detector(self):
        pass

#detect if card placed after challenge card is another challenge card
    def battle(self):
        pass

#----------------------------------------------------------------------------------------

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("this is a test")
    screen = pygame.display.set_mode((2000, 1000))
    #---------------set up----------------------------------------------------------------------------set up








    #-----------------------------------------------------------------------------------------------------------
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == QUIT:
                sys.exit()
            #-----in for loop------------------------------------------------------------------------------in for event loop



        #------------out of for loop-------------------------------------------------------------------out of for event loop
        screen.fill((220, 181, 121))
        pressed_keys = pygame.key.get_pressed()















        pygame.display.update()

main()