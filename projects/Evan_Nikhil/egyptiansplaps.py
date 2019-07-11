import pygame, sys, random, time
from pygame.locals import *

#-----------------------------------------------------------------------------Player
class Player:
    def __init__(self,deck):
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

#-----------------------------------------------------------------------------------------

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("this is a test")
    screen = pygame.display.set_mode((2000, 1000))
    #---------------set up----------------------------------------------------------------------------set up
    #setting up new deck and dealing out cards
    new_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
    temp_deck = []
    random.shuffle(new_deck)
    print(len(new_deck))
    print(new_deck)
    for i in range(18):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player1 = Player(temp_deck)
    temp_deck = []
    #player2
    #player3








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