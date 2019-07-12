import pygame, sys, random, time
from pygame.locals import *

#-----------------------------------------------------------------------------Player
class Player:
    def __init__(self, deck):
        self.deck = deck
        self.is_playing = True

    #add top card of deck to pot then remove card from deck
    def place_card(self, center_pile):
        center_pile.add_card(self.deck.pop(0))
        self.is_playing = len(self.deck) > 0

    def discard_card(self, center_pile):
        center_pile.bury_card(self.deck.pop(0))
        self.is_playing = len(self.deck) > 0

#---------------------------------------------------------------------------------------CenterPile
class CenterPile:
    def __init__(self):
        self.cards = []
        self.is_slap_allowed = False

    def add_card(self, new_card):
        self.cards.append(new_card)
        self.is_slap_allowed = False
        print(self.cards)
        if len(self.cards) > 1:
            if self.cards[-1] == self.cards[-2]:
                print("Slap is allowed")
                self.is_slap_allowed = True

        if len(self.cards) > 2:
            if self.cards[-1] == self.cards[-3]:
                print("Slap is allowed")
                self.is_slap_allowed = True


class TurnController:
    def __init__(self, player1, player2, player3):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.previous_turn = -1
        self.current_turn = 1

    def next_turn(self):
        self.previous_turn = self.current_turn
        if self.current_turn == 1:
            if self.player2.is_playing:
                self.current_turn = 2
            else:
                self.current_turn = 3
        elif self.current_turn == 2:
            if self.player3.is_playing:
                self.current_turn = 3
            else:
                self.current_turn = 1
        elif self.current_turn == 3:
            if self.player1.is_playing:
                self.current_turn = 1
            else:
                self.current_turn = 2

    def get_current_player(self):
        if self.current_turn == 1:
            return self.player1

        if self.current_turn == 2:
            return self.player2

        if self.current_turn == 3:
            return self.player3


    def get_previous_player(self):
        if self.previous_turn == 1:
            return self.player1

        if self.previous_turn == 2:
            return self.player2

        if self.previous_turn == 3:
            return self.player3




# #----------------------------------------------------------------------------- reset functions

def slap(player, center_pile):
    print("slap")
    print(player.deck)
    print(center_pile.cards)
    if center_pile.is_slap_allowed:
        player.deck = player.deck + center_pile.cards
        center_pile.cards = []

    else:
        player.discard_card(center_pile)


    print(player.deck)
    print(center_pile.cards)


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
    turn_controller = TurnController(player1, player2, player3)

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
                if turn_controller.current_turn == 1:
                    print("Player 1 play card")
                    turn_controller.next_turn()
                    player1.place_card(center_pile)
                else:
                    print("It is not player 1's turn")




            if pressed_keys[pygame.K_1]:
                print('1')
                slap(player1, center_pile)

            if pressed_keys[pygame.K_v]:
                print('v')
                if turn_controller.current_turn == 2:
                    print("Player 2 play card")
                    turn_controller.next_turn()
                    player2.place_card(center_pile)
                else:
                    print("It is not player 2's turn.")

            if pressed_keys[pygame.K_b]:
                print('b')


            if pressed_keys[pygame.K_o]:
                print('o')
                if turn_controller.current_turn == 3:
                    print("Player 3 play card")
                    turn_controller.next_turn()
                    player3.place_card(center_pile)
                else:
                    print("It is not player 3's turn.")

            if pressed_keys[pygame.K_p]:
                print('p')

        #------------out of for loop--------------------------------------------------------------------out of for event loop
        screen.fill((220, 181, 121))

        pygame.display.update()

main()