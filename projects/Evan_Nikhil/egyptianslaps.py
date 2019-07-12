import pygame, sys, random, time
from pygame.locals import *
from threading import Lock

#-------------------------------------------------------------------------------Challenge
class Challenge:
    def __init__(self,centerPile,turn_controler):
        self.top_card = centerPile.card[-1]
        self.trys = 0
        self.turn_controler = turn_controler


#detect to set up tries remaining
    def card_detector(self):
        #seeing if a chalang is played and what type
        if self.top_card == 'J':
            self.trys = 1
            #self.battle
            return True

        elif self.top_card == 'Q':
            self.trys = 2
            return True
        elif self.top_card == 'K':
            self.trys = 3
            return True
        elif self.top_card == 'A':
            self.trys = 4
            return True
        else:
            return False


#detect if card placed after challenge card is another challenge card
    def battle(self,player,turn):
        pass
        # if the chalenger secseeds
        if self.card_detector():
            pass
            #next players turn
        #if they fail and still have trys
        elif not self.trys == 0:
            self.trys -= 1
        # if they fail and have no trys left
        else:
            #previus player reword
            #reset round
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


# #---------------------------------------------------------------------------------------------- board controller
class BoardController:
    def __init__(self,screen,card_image,hand_image,caption_font, slap_sound):
        self.screen = screen
        self.card_image = card_image
        self.hand_image1 = pygame.transform.rotate(hand_image, 270)
        self.hand_image2 = pygame.transform.rotate(hand_image, 0)
        self.hand_image3 = pygame.transform.rotate(hand_image, 90)
        self.hand_location = [(300,230),(395,270),(450,230)]
        self.card_location = [[50,289],[430,578],[810,289],[310,289],[340,289],[370,289],[400,289],[430,289]]
        self.show_cards = caption_font.render("429A10", True, (0,0,0))
        self.caption_font = caption_font
        self.temp_storage = 0
        self.who_slapped = [0,0,0]
        self.slap_sound =  slap_sound
#there are sooooooo many variables that this needs, this is crazy it is 12 btw

    def set_up_board(self,deck,hands):
        self.screen.fill((220, 181, 121))
# setting up the rules to the game so that the players know what to do---------------------------------------------------------
        self.temp_storage = self.caption_font.render("rule of the game: player one slaps with ` and places a card with 1 ", True, (0, 0, 0))
        self.screen.blit(self.temp_storage, (10,10))
        self.temp_storage = self.caption_font.render("player two slaps with v and places a card with b", True, (0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 30))
        self.temp_storage = self.caption_font.render("player two slaps with o and places a card with p", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 50))
        self.temp_storage = self.caption_font.render("when two of a kind or two of a kind with one in the middle appears, slap to win the round", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 70))
        self.temp_storage = self.caption_font.render("when a J,Q,K, or A show up the next player is challenged, if you fail the chalenge the ", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 90))
        self.temp_storage = self.caption_font.render("chalenger wins, if you secseed then you chalenge the next person in line", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 110))
        self.temp_storage = self.caption_font.render("to win a chalenge you need to play a J,Q,K, or A and depending on the card you get only", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 130))
        self.temp_storage = self.caption_font.render("so many tries. 1 for J, 2 for Q, 3 for K, and 4 for A.", True, (0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 150))

        # set up where the cards are placed-------------------------------------------------------------------
        for i in range(8):
            pygame.draw.rect(self.screen, (0, 0, 0),((self.card_location[i][0] - 22, self.card_location[i][1] - 22), (144, 177)))
            pygame.draw.rect(self.screen, (252, 252, 252), ((self.card_location[i][0] - 20,self.card_location[i][1] - 20), (140, 173)))
            self.screen.blit(self.card_image, (self.card_location[i][0],self.card_location[i][1]))
        #set up the numbers on the cards-------------------------------------------------------------------
        if len(deck) < 5:
            # this is for if the deck is less then 5
            for i in range(len(deck)):
                self.show_cards = self.caption_font.render(str(deck[(-1*(len(deck))+i)]), True, (0, 0, 0))
                self.screen.blit(self.show_cards,(self.card_location[i+(8-len(deck))][0] - 18,self.card_location[i+(8-len(deck))][1] - 20))
        else:
            #this if for if the deck is 5 or more
            for i in range(5):
                self.show_cards = self.caption_font.render(str(deck[(-5 + i)]), True, (0, 0, 0))
                self.screen.blit(self.show_cards,(self.card_location[i + 3][0] - 18, self.card_location[i + 3][1] - 20))
# the hands---------------------------------------------------------------------------------------------
        # todo set up a thing to have slaps
        if self.who_slapped[0] == 1:
            self.screen.blit(self.hand_image1, self.hand_location[0])
        if self.who_slapped[1] == 1:
            self.screen.blit(self.hand_image2, self.hand_location[1])
        if self.who_slapped[2] == 1:
            self.screen.blit(self.hand_image3, self.hand_location[2])
# saying how many cards everyone has-------------------------------------------------------------------
        for i in range(3):
            self.temp_storage = self.caption_font.render("cards in hand:" + str(hands[i]), True, (0, 0, 0))
            self.screen.blit(self.temp_storage,(self.card_location[i][0]-25 ,self.card_location[i][1] - 40))

# seting up slapping vishuwal and sounds
    #todo add this to the begining and end of the slap lines
    def hand_slap(self,player_number):
        self.slap_sound.play(1)
        if self.who_slapped[player_number-1] == 0:
            self.who_slapped[player_number-1] = 1
        else:
            self.who_slapped[player_number - 1] = 0

#----------------------------------------------------------------------------------------
def main():
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("this is a test")
    screen = pygame.display.set_mode((1000, 750))

    #---------------set up---------------------------------------------------------------------------------------------------------------set up
    slap_sound = pygame.mixer.Sound("slap.wav")
    slap_hand = pygame.image.load('slap_hand2..png')
    slap_hand.set_colorkey(pygame.Color('WHITE'))
    card_image = pygame.image.load('card.jpeg')
    card_image = pygame.transform.scale(card_image, (100, 133))
    caption_font = pygame.font.Font(None, 28)
    #challenge = Challenge(turn_controller.current_turn)

    board_controller = BoardController(screen,card_image,slap_hand,caption_font, slap_sound)








    turn = 1
    last5cards = [0,0,0,0,0]
    pot = []
    first_player_pressed = False
    centerpile = CenterPile()





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






    #--------------------------------------------------------------------------------------------------------------------------

    while True:
        clock.tick(60)
        pressed_keys = pygame.key.get_pressed()

        board_controller.set_up_board([5,"A", 4],[40,10,50])
        #board_controller.set_up_board(center_pile.deck, [player1.deck, player2.deck, player3.deck])




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

        pressed_keys = pygame.key.get_pressed()















        pygame.display.update()

main()