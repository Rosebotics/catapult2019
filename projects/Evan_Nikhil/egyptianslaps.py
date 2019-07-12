import pygame, sys, random, time
from pygame.locals import *
from threading import Lock

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
    def __init__(self,player1,player2,player3):
        self.order_of_slaps = []
        self.round_winner = 0
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3



    def slap(self,time,last5cards,pot):
       # while time+1000 > time.time() :
            #todo add a wait here till no one has slapped for one second
        print("i got to step one")
        print(self.order_of_slaps)
        if last5cards[4] == last5cards[3] or last5cards[4] == last5cards [2]:
            self.round_winner = self.order_of_slaps[0]
            print('i am about to freek out')
            self.win(self.round_winner,pot)
          #  new_round()

    def win(self,winner,pot):
        if winner == 1:
            self.player1.deck.append(pot)
            print("i did not die")
        self.order_of_slaps = []


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
    def place_card(self,pot,last5cards):
        pot.append(self.deck[0])
        #TODO remove the print and print
        last5cards.append(self.deck[0])
        self.deck.pop(0)
        #print(pot)
        #print(self.deck)
      #  print(last5cards)

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


# #----------------------------------------------------------------------------- reset functions



#----------------------------------------------------------------------------------------
def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("this is a test")
    screen = pygame.display.set_mode((500, 500))

    #---------------set up----------------------------------------------------------------------------set up
    turn = 1
    last5cards = [0,0,0,0,0]
    pot = []
    first_player_pressed = False
    centerpile = CenterPile()

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
    detection = Detection(player1,player2,player3)






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
            #todo set up next turn
            if not first_player_pressed:
                if pressed_keys[pygame.K_BACKQUOTE] and turn == 1:
                    print(new_deck)
                    turn = 2
                    player1.place_card(pot,last5cards)

                if pressed_keys[pygame.K_v] and turn == 2:
                   # print(new_deck)
                    turn = 3
                    player2.place_card(pot,last5cards)

                if pressed_keys[pygame.K_o] and turn == 3:
                    #print(new_deck)
                    turn = 1
                    player3.place_card(pot,last5cards)
                #button presses for slapping
                #todo remove Prints
                #todo set up player 2 and 3 slap
                if pressed_keys[pygame.K_1]:
                    print('begin long sleep')
                    first_player_pressed = True
                    time.sleep(2)
                    player1.slap()
                    detection.order_of_slaps.append(1)
                    detection.slap(time.time(),last5cards,pot)
                    first_player_pressed = False


                if pressed_keys[pygame.K_b]:
                    print('b')
                    first_player_pressed = True
                    time.sleep(2)
                    player2.slap()
                    detection.order_of_slaps.append(2)
                    detection.slap(time.time(), last5cards, pot)
                    first_player_pressed = False

                if pressed_keys[pygame.K_p]:
                    print('p')
                    first_player_pressed = True
                    time.sleep(2)
                    player3.slap()
                    detection.order_of_slaps.append(3)
                  #  print(detection.order_of_slaps)
                    detection.slap(time.time(), last5cards, pot)
                    first_player_pressed = False



        #------------out of for loop--------------------------------------------------------------------out of for event loop
        screen.fill((220, 181, 121))
        pressed_keys = pygame.key.get_pressed()















        pygame.display.update()

main()