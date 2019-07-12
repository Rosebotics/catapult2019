import pygame, sys, random, time
from pygame.locals import *

#-----------------------------------------------------------------------------Player
class Player:
    def __init__(self, deck):
        self.deck = deck
        self.in_out = True

    #add top card of deck to pot then remove card from deck
    def place_card(self, center_pile):
        center_pile.add_card( self.deck.pop(0))

#---------------------------------------------------------------------------------------CenterPile
class CenterPile:
    def __init__(self):
        self.cards = []
        self.is_slap_allowed = False

    def add_card(self, new_card):
        self.cards.append(new_card)
        self.is_slap_allowed = False
        if len(self.cards) > 1:
            if self.cards[-1] == self.cards[-2]
                print("Slap is allowed")
                self.is_slap_allowed = True



# #----------------------------------------------------------------------------- reset functions


#----------------------------------------------------------------------------------------
def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Egyptian Rat Killer")
    screen = pygame.display.set_mode((500, 500))

    #---------------set up----------------------------------------------------------------------------set up

    #setting up new deck and dealing out cards
    new_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
    temp_deck = []
    random.shuffle(new_deck)
    for i in range(18):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player1 = Player(temp_deck)
    temp_deck = []

    #player2
    for i in range(17):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player2 = Player(temp_deck)
    temp_deck = []

    #player3
    for i in range(17):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player3 = Player(temp_deck)

    print(player1.deck)
    print(player2.deck)
    print(player3.deck)

    # --------------------------------- Setup Centerpile -----------------------------------------
    center_pile = CenterPile()

    #--------------------------------------------------------------------------------------------------------


    #-----------------------------------------------------------------------------------------------------------

    while True:
        clock.tick(60)
        pressed_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if pressed_keys[pygame.K_BACKQUOTE]:
                print('`')
                print("Player 1 play card")
                player1.place_card(center_pile)

            if pressed_keys[pygame.K_1]:
                print('1')

            if pressed_keys[pygame.K_v]:
                print('v')
            if pressed_keys[pygame.K_b]:
                print('b')

            if pressed_keys[pygame.K_o]:
                print('o')
            if pressed_keys[pygame.K_p]:
                print('p')

        #------------out of for loop--------------------------------------------------------------------out of for event loop
        screen.fill((220, 181, 121))

        pygame.display.update()

main()