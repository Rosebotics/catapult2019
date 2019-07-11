import pygame, sys, random, time
from pygame.locals import *

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

#-----------------------------------------------------------------------------------Detection
class Detection:
    def __init__(self):
        self.last5cards = []
        self.order_of_slaps = []
        self.round_winner = 0



    def slap(self):
        pass

    def win(self):
        pass

    def new_round(self):
        pass

#-----------------------------------------------------------------------------Player
class Player:
    def __init__(self,deck):
        self.deck = deck
        self.in_out = True
        self.slap_time = 0
        self.have_slapped = False


#add top card of deck to pot then remove card from deck
    def place_card(self,pot):
        pot.append(self.deck[0])
        self.deck.pop(0)
        #TODO remove the print and prints
        print(pot)
        print(self.deck)

    def slap(self):
        #add name to list and then say that you have slapped
        self.have_slapped = True

    def draw(self):
        pass

#---------------------------------------------------------------------------------------CenterPile
class CenterPile:
    def __init__(self):
        pass

    def draw(self):
        pass

#-----------------------------------------------------------------------------------------

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("this is a test")
    screen = pygame.display.set_mode((500, 500))
    #---------------set up----------------------------------------------------------------------------set up
    turn = 1
    pot = []
    centerpile = CenterPile()
    detection = Detection()
    challenge = Challenge()



    #setting up new deck and dealing out cards
    new_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
    temp_deck = []
    random.shuffle(new_deck)
    #done remove prints
   # print(len(new_deck))
    #print(new_deck)
    for i in range(18):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player1 = Player(temp_deck)
  # print(temp_deck)
    temp_deck = []

    #player2
    for i in range(17):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player2 = Player(temp_deck)
  #  print(temp_deck)
    temp_deck = []

    #player3
    for i in range(17):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player3 = Player(temp_deck)
   # print(temp_deck)
    temp_deck = []

    #--------------------------------------------------------------------------------------------------------







    #-----------------------------------------------------------------------------------------------------------

    while True:
        clock.tick(60)
        pressed_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            #-----in for loop------------------------------------------------------------------------------in for event loop
           #done remove prints
            # this is button detection for card placement
            if pressed_keys[pygame.K_BACKQUOTE] and turn == 1:
                #print(new_deck)
                turn = 2
                player1.place_card(pot)

            if pressed_keys[pygame.K_v] and turn == 2:
               # print(new_deck)
                turn = 3
                player2.place_card(pot)

            if pressed_keys[pygame.K_o] and turn == 3:
                #print(new_deck)
                turn = 1
                player3.place_card(pot)
            #button presses for slapping
            #todo remove Prints
            if pressed_keys[pygame.K_1]:
                print('1')
                player1.slap()
                detection.order_of_slaps.append(1)


            if pressed_keys[pygame.K_b]:
                print('b')
                player2.slap()
                detection.order_of_slaps.append(2)

            if pressed_keys[pygame.K_p]:
                print('p')
                player3.slap()
                detection.order_of_slaps.append(3)
                print(detection.order_of_slaps)



        #------------out of for loop--------------------------------------------------------------------out of for event loop
        screen.fill((220, 181, 121))
        pressed_keys = pygame.key.get_pressed()















        pygame.display.update()

main()