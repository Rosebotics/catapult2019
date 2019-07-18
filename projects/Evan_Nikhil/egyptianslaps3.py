import pygame, sys, random, time
from pygame.locals import *

#-----------------------------------------------------------------------------Player
class Player:
    def __init__(self, deck, player_number):
        self.deck = deck
        self.is_playing = True
        self.player_number = player_number

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
#add cards
    def add_card(self, new_card):
        self.cards.append(new_card)
        self.is_slap_allowed = False
        # seeing for slaps
        if len(self.cards) > 1:
            if self.cards[-1] == self.cards[-2]:
                self.is_slap_allowed = True

        if len(self.cards) > 2:
            if self.cards[-1] == self.cards[-3]:
                self.is_slap_allowed = True
       # print(self.cards)
# punishing miss slaps
    def bury_card(self, new_card):
        self.cards.insert(0, new_card)
       # print(self.cards)
# seeing what the top card is
    def get_top_card(self):
        if len(self.cards) > 0:
            return self.cards[-1]
# empting deck
    def empty_deck(self):
        self.cards = []
        self.is_slap_allowed = False


#--------------------------------------------------------------------------------------turn controler
class TurnController:
    def __init__(self, player1, player2, player3):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.previous_turn = -1
        self.current_turn = 1
# set whos turn it is  at first
    def set_turn_to(self, new_player_turn):
        self.previous_turn = self.current_turn
        self.current_turn = new_player_turn
# setting the next turn
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
# retun whos turn it is
    def get_current_player(self):
        if self.current_turn == 1:
            return self.player1
        if self.current_turn == 2:
            return self.player2
        if self.current_turn == 3:
            return self.player3
# say who the previus player turn is
    def get_previous_player(self):
        if self.previous_turn == 1:
            return self.player1
        if self.previous_turn == 2:
            return self.player2
        if self.previous_turn == 3:
            return self.player3


# -------------------------------------------------------------------------------Challenge
class ChallengeController:
    def __init__(self, center_pile, turn_controller, player1, player2, player3):
        self.center_pile = center_pile
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.tries = -1
        self.turn_controller = turn_controller
        self.is_challenge_active = False
        self.challenger = None
        self.challengee = None
        self.delay_challenge_loss = -1


    def possible_challenge(self):
        # assumes a card has just been played and there is no active challenge it moves on to the next player.
        top_card = self.center_pile.get_top_card()
        is_new_challenge = False
        # set up the trys
        if top_card == 'J':
            self.tries = 1
            is_new_challenge = True
        elif top_card == 'Q':
            self.tries = 2
            is_new_challenge = True
        elif top_card == 'K':
            self.tries = 3
            is_new_challenge = True
        elif top_card == 'A':
            self.tries = 4
            is_new_challenge = True
#start up the chalange
        if is_new_challenge:
            self.is_challenge_active = True
            self.challenger = self.turn_controller.get_current_player()
            self.turn_controller.next_turn()
            self.challengee = self.turn_controller.get_current_player()
        else:
            self.turn_controller.next_turn()

    def attempt(self):
        # print('before')
        # print("   self.is_challenge_active", self.is_challenge_active)
        # print("   self.tries", self.tries)
        # print("   self.challenger.player_number", self.challenger.player_number)
        # print("   self.challengee.player_number", self.challengee.player_number)

        # assumes a card has just been played during an active challenge and resolves the challenge or continues it.
        top_card = self.center_pile.get_top_card()
        # if the chalengd secseeds
        if top_card == 'J' or top_card == 'Q' or top_card == 'K' or top_card == 'A':
            self.is_challenge_active = False
            self.possible_challenge()
        else:
            # if they fail
            self.tries = self.tries - 1
            if self.tries == 0:
                self.delay_challenge_loss = 60
            elif not self.challengee.is_playing:
               # print('challengee ran out of cards')
                self.turn_controller.next_turn()
                self.challengee = self.turn_controller.get_current_player()
        # print('after')
        # print("   self.is_challenge_active", self.is_challenge_active)
        # print("   self.tries", self.tries)
        # print("   self.challenger.player_number", self.challenger.player_number)
        # print("   self.challengee.player_number", self.challengee.player_number)

    # done Consider giving people a chance to slap while challenge is going on.
    def resolve_lost_challenge(self):
        self.challenger.deck = self.challenger.deck + self.center_pile.cards
        self.challenger.is_playing = True
        self.center_pile.empty_deck()
        self.turn_controller.set_turn_to(self.challenger.player_number)
        self.is_challenge_active = False
        self.delay_challenge_loss = -1


# #----------------------------------------------------------------------------- functions

def slap(player, center_pile, turn_controller, challenge_controller):
   # not allowing people who are out to slap
    if not player.is_playing:
        if not (challenge_controller.is_challenge_active and challenge_controller.challenger.player_number == player.player_number):
            return
    #if slap it allowed
    if center_pile.is_slap_allowed:
        challenge_controller.is_challenge_active = False
        player.deck = player.deck + center_pile.cards
        center_pile.empty_deck()
        turn_controller.set_turn_to(player.player_number)
        challenge_controller.delay_challenge_loss = -1
       # print(center_pile.cards)
    else:
        if len(center_pile.cards) > 1 and player.is_playing:
            player.discard_card(center_pile)
            if not player.is_playing:
                turn_controller.next_turn()


def play_card(player, center_pile, turn_controller, challenge_controller):
    if challenge_controller.delay_challenge_loss > 0:
        return
    if turn_controller.current_turn == player.player_number:
        player.place_card(center_pile)
        if challenge_controller.is_challenge_active:
            challenge_controller.attempt()
        else:
            challenge_controller.possible_challenge()
    else:
       print("It is not this player's turn")


def check_for_game_over(challenge_controller):
    is_game_over = True
    is_player_1_active = False
    is_player_2_active = False
    is_player_3_active = False
    if challenge_controller.player1.is_playing:
        is_player_1_active = True
    elif challenge_controller.is_challenge_active and challenge_controller.challenger.player_number == 1:
        is_player_1_active = True

    if challenge_controller.player2.is_playing:
        is_player_2_active = True
    elif challenge_controller.is_challenge_active and challenge_controller.challenger.player_number == 2:
        is_player_2_active = True

    if challenge_controller.player3.is_playing:
        is_player_3_active = True
    elif challenge_controller.is_challenge_active and challenge_controller.challenger.player_number == 3:
        is_player_3_active = True

    # if is_player_1_active:
    #     print('1', end='')
    # if is_player_2_active:
    #     print('2', end='')
    # if is_player_3_active:
    #     print('3', end='')
    # print()

    if is_player_1_active and is_player_2_active:
        is_game_over = False
    if is_player_2_active and is_player_3_active:
        is_game_over = False
    if is_player_3_active and is_player_1_active:
        is_game_over = False

    return is_game_over
#---------------------------------------------------------------------------------------------- board controller
class BoardController:
    def __init__(self,screen,card_image,card_back_image,hand_image,caption_font, slap_sound):
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
        self.card_back_image = card_back_image
        self.moveing_x = 0
        self.moveing_y = 0

#there are sooooooo many variables that this needs, this is crazy it is 12 btw

    def set_up_board(self,deck,hands,current_turn,trys):
        self.screen.fill((220, 181, 121))
# setting up the rules to the game so that the players know what to do---------------------------------------------------------
        self.temp_storage = self.caption_font.render("Rule of the Game:      Player One places a card with ~ and slaps with 1 ", True, (0, 0, 0))
        self.screen.blit(self.temp_storage, (10,10))
        self.temp_storage = self.caption_font.render("Player Two places a card with v and slaps with b", True, (0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 30))
        self.temp_storage = self.caption_font.render("Player Three places a card with o and slaps with p ", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 50))
        self.temp_storage = self.caption_font.render("When two of a kind or two of a kind with a random card in the middle appears, slap to win the round", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 70))
        self.temp_storage = self.caption_font.render("If you slap at the wrong time you will be penalized, You will lose the top card of your hand", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 90))
        self.temp_storage = self.caption_font.render("When J,Q,K, or A show up, the next player is challenged. To win a challenge you need to play a J,Q,K, or A", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 110))
        self.temp_storage = self.caption_font.render("and depending on the card you play, only get so many tries. 1 for J, 2 for Q, 3 for K, and 4 for A. ", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 130))
        self.temp_storage = self.caption_font.render("If you fail the challenge, the challenger wins, If you succeed, then you challenge the next person in line.", True,(0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 150))
        self.temp_storage = self.caption_font.render("press T to make the game two player", True, (0, 0, 0))
        self.screen.blit(self.temp_storage, (172, 170))
#If you fail the challenge, the    challenger wins, If you succeed, then you challenge the next person in line.
        # set up where the cards are placed-------------------------------------------------------------------
        if not (hands[0] == 0):
            pygame.draw.rect(self.screen, (0, 0, 0),((self.card_location[0][0] - 22, self.card_location[0][1] - 22), (144, 177)))
            pygame.draw.rect(self.screen, (252, 252, 252), ((self.card_location[0][0] - 20,self.card_location[0][1] - 20), (140, 173)))
            self.screen.blit(self.card_image, (self.card_location[0][0],self.card_location[0][1]))
        if not (hands[1] == 0):
            pygame.draw.rect(self.screen, (0, 0, 0),((self.card_location[1][0] - 22, self.card_location[1][1] - 22), (144, 177)))
            pygame.draw.rect(self.screen, (252, 252, 252),((self.card_location[1][0] - 20, self.card_location[1][1] - 20), (140, 173)))
            self.screen.blit(self.card_image, (self.card_location[1][0], self.card_location[1][1]))
        if not hands[2] == 0:
            pygame.draw.rect(self.screen, (0, 0, 0),((self.card_location[2][0] - 22, self.card_location[2][1] - 22), (144, 177)))
            pygame.draw.rect(self.screen, (252, 252, 252),((self.card_location[2][0] - 20, self.card_location[2][1] - 20), (140, 173)))
            self.screen.blit(self.card_image, (self.card_location[2][0], self.card_location[2][1]))


        #putting the correct amount of cards in the center
        if len(deck) < 5:
            for i in range(len(deck)):
                pygame.draw.rect(self.screen, (0, 0, 0),((self.card_location[3+i][0] - 22, self.card_location[3+i][1] - 22), (144, 177)))
                pygame.draw.rect(self.screen, (252, 252, 252), ((self.card_location[3+i][0] - 20,self.card_location[3+i][1] - 20), (140, 173)))
                self.screen.blit(self.card_back_image, (self.card_location[3+i][0],self.card_location[3+i][1]))
        else:
            for i in range(5):
                pygame.draw.rect(self.screen, (0, 0, 0),((self.card_location[3+i][0] - 22, self.card_location[3+i][1] - 22), (144, 177)))
                pygame.draw.rect(self.screen, (252, 252, 252), ((self.card_location[3+i][0] - 20,self.card_location[3+i][1] - 20), (140, 173)))
                self.screen.blit(self.card_back_image, (self.card_location[3+i][0],self.card_location[3+i][1]))
        #set up the numbers on the cards-------------------------------------------------------------------
        if len(deck) < 5:
            # this is for if the deck is less then 5
            for i in range(len(deck)):
                self.show_cards = self.caption_font.render(str(deck[(-1*(len(deck))+i)]), True, (0, 0, 0))
                self.screen.blit(self.show_cards,(self.card_location[i+3][0] - 18,self.card_location[i+3][1] - 18))
        else:
            #this if for if the deck is 5 or more
            for i in range(5):
                self.show_cards = self.caption_font.render(str(deck[(-5 + i)]), True, (0, 0, 0))
                self.screen.blit(self.show_cards,(self.card_location[i + 3][0] - 18, self.card_location[i + 3][1] - 18))
            #says whos turn it is
        if current_turn == 1:
            pygame.draw.polygon(self.screen,(0,0,0), ((410,225),(410,245),(390,235)))
        if current_turn == 2:
            pygame.draw.polygon(self.screen, (0, 0, 0), ((460, 245), (480, 245), (470, 265)))
        if current_turn == 3:
            pygame.draw.polygon(self.screen, (0, 0, 0), ((530, 225), (530, 245), (550, 235)))
        self.temp_storage = self.caption_font.render("Player" + str(current_turn) + "'s turn", True, (0, 0, 0))
        self.screen.blit(self.temp_storage, (420, 230))

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
            self.temp_storage = self.caption_font.render("Player " + str(i+1), True, (0, 0, 0))
            self.screen.blit(self.temp_storage, (self.card_location[i][0] - 20, self.card_location[i][1] - 60))
            self.temp_storage = self.caption_font.render("Cards in hand:" + str(hands[i]), True, (0, 0, 0))
            self.screen.blit(self.temp_storage,(self.card_location[i][0]-25 ,self.card_location[i][1] - 40))
#---------------------------desplaying the amount of trys the player has left---------
        if trys > 0:
            self.temp_storage = self.caption_font.render("Player " + str(current_turn) + " has "+ str(trys) + " tries left", True, (0, 0, 0))
            self.screen.blit(self.temp_storage, (400,200))

# seting up slapping vishuwal and sounds
    #todo add this to the begining and end of the slap lines
    def hand_slap(self,player_number):
        if player_number == 4:
            self.who_slapped[0] = 0
            self.who_slapped[1] = 0
            self.who_slapped[2] = 0
        elif self.who_slapped[player_number - 1] == 0:
            self.slap_sound.play()
            self.who_slapped[player_number - 1] = 1

# the game over screen
    def game_over_screen(self,winner):
        self.screen.fill((220, 181, 121))

        for i in range (10):
            if (i % 2) == 0:
                self.screen.blit(self.card_image,((i * 100),self.moveing_y))
            else:
                self.screen.blit(self.card_back_image,(i * 100, self.moveing_y))
        for i in range (5):
            if (i % 2) == 0:
                self.screen.blit(self.card_image, (self.moveing_x, i*133))
            else:
                self.screen.blit(self.card_back_image, (self.moveing_x, i*133))
        for i in range (5):
            if (i % 2) == 1:
                self.screen.blit(self.card_image, (self.screen.get_width() - self.moveing_x, i*133))
            else:
                self.screen.blit(self.card_back_image, (self.screen.get_width() - self.moveing_x, i*133))

        for i in range (10):
            if (i % 2) == 0:
                self.screen.blit(self.card_image,((i * 100),self.screen.get_height() - self.moveing_y))
            else:
                self.screen.blit(self.card_back_image,(i * 100, self.screen.get_height() - self.moveing_y))
        pygame.draw.rect(self.screen,(220, 181, 121),((340,335),(325,60)))
        self.temp_storage = self.caption_font.render('Player '+str(winner)+ " is the winner", True, (255, 255, 255))
        self.screen.blit(self.temp_storage, (410, 335))
        self.temp_storage = self.caption_font.render("everyone else has disturbed the pharaoh", True, (255, 255, 255))
        self.screen.blit(self.temp_storage, (340, 355))
        self.temp_storage = self.caption_font.render("press space to restart the game", True, (255, 255, 255))
        self.screen.blit(self.temp_storage, (380, 375))
        self.moveing_x += 2
        self.moveing_y += 1
        if self.moveing_x > self.screen.get_width():
            self.moveing_x = 0
        if self.moveing_y > self.screen.get_height():
            self.moveing_y = 0




# the reset code for the new game ----------------------------------------------------------------------------
def new_game(player1,player2,player3, center_pile,challenge_controller):
    new_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']
    temp_deck = []
    random.shuffle(new_deck)
    for i in range(18):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player1.deck = temp_deck
    temp_deck = []

    # player2
    for i in range(17):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player2.deck = temp_deck
    temp_deck = []

    # player3
    for i in range(17):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player3.deck = temp_deck

    center_pile.empty_deck()
    player1.is_playing = True
    player2.is_playing = True
    player3.is_playing = True
    challenge_controller.is_challenge_active = False

#--------------------------------------------------setting as two player mode
def two_Player(player1,player2,player3):
    give_player = 1
    for i in range(len(player2.deck)):
        if give_player == 1:
            give_player = 2
            player3.deck.append(player2.deck[0])
            player2.deck.pop(0)
        elif give_player == 2:
            give_player = 1
            player1.deck.append(player2.deck[0])
            player2.deck.pop(0)


#----------------------------------------------------------------------------------------
def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Egyptian Rat slap")
    screen = pygame.display.set_mode((1000, 750))
    card_delay = -1
    dev_restart = 0

    #---------------set up----------------------------------------------------------------------------set up

    #setting up new deck and dealing out cards
    new_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
    temp_deck = []
    random.shuffle(new_deck)
    for i in range(18):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player1 = Player(temp_deck, 1)
    temp_deck = []

    #player2
    for i in range(17):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player2 = Player(temp_deck, 2)
    temp_deck = []

    #player3
    for i in range(17):
        temp_deck.append(new_deck[0])
        new_deck.pop(0)
    player3 = Player(temp_deck, 3)

    print(player1.deck)
    print(player2.deck)
    print(player3.deck)
    turn_controller = TurnController(player1, player2, player3)

    # --------------------------------- Setup Centerpile -----------------------------------------
    center_pile = CenterPile()
    challenge_controller = ChallengeController(center_pile, turn_controller, player1, player2, player3)

    #--------------------------------------------------------------------------------------------------------
    slap_sound = pygame.mixer.Sound("slap.wav")
    slap_hand = pygame.image.load('slap_hand2..png')
    slap_hand.set_colorkey(pygame.Color('WHITE'))
    card_image = pygame.image.load('card.jpeg')
    card_image = pygame.transform.scale(card_image, (100, 133))
    caption_font = pygame.font.Font(None, 24)
    card_back_image = pygame.image.load('card_back.jpg')
    card_back_image = pygame.transform.scale(card_back_image, (100, 133))

    board_controller = BoardController(screen,card_image,card_back_image, slap_hand,caption_font, slap_sound)

    #-----------------------------------------------------------------------------------------------------------
    is_game_over = False
    has_displayed_game_over = False

    while True:
        clock.tick(60)

        pressed_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if not is_game_over:
                # debut and complex not during bame buttons
                if pressed_keys[pygame.K_t] and len(player2.deck) == 17 and len(player3.deck) == 17 and len(player1.deck) == 18:
                    two_Player(player1,player2,player3)
                    player2.is_playing = False
                if pressed_keys[pygame.K_e] and len(player2.deck) == 17 and len(player3.deck) == 17 and len(player1.deck) == 18:
                    player1.deck = [5,5,"J","A"]
                    player2.deck = [5,6,"Q",4,3,2,1]
                    player3.deck = [5,"K"]
                # deve reset
                if pressed_keys[pygame.K_r]:
                    dev_restart = 1
                if pressed_keys[pygame.K_e] and dev_restart == 1:
                    dev_restart = 2
                if pressed_keys[pygame.K_s] and dev_restart == 2:
                    dev_restart = 3
                if pressed_keys[pygame.K_t] and dev_restart == 3:
                    dev_restart = 0
                    new_game(player1, player2, player3, center_pile, challenge_controller)
                    is_game_over = False
                    has_displayed_game_over = False
                    board_controller.moveing_x = 0
                    board_controller.moveing_y = 0
                    turn_controller.set_turn_to(1)
                    #normal game buttons
                if pressed_keys[pygame.K_BACKQUOTE] and card_delay < 1:
                    board_controller.hand_slap(4)
                    card_delay = 5
                    dev_restart = 0
                    play_card(player1, center_pile, turn_controller, challenge_controller)
                    is_game_over = check_for_game_over(challenge_controller)
                if pressed_keys[pygame.K_1]:
                    board_controller.hand_slap(1)
                    slap(player1, center_pile, turn_controller, challenge_controller)
                    is_game_over = check_for_game_over(challenge_controller)
                if pressed_keys[pygame.K_v]and card_delay < 1:
                    board_controller.hand_slap(4)
                    card_delay = 5
                    dev_restart = 0
                    play_card(player2, center_pile, turn_controller, challenge_controller)
                    is_game_over = check_for_game_over(challenge_controller)
                if pressed_keys[pygame.K_b]:
                    board_controller.hand_slap(2)
                    slap(player2, center_pile, turn_controller, challenge_controller)
                    is_game_over = check_for_game_over(challenge_controller)
                if pressed_keys[pygame.K_o]and card_delay < 1:
                    board_controller.hand_slap(4)
                    card_delay = 5
                    dev_restart = 0
                    play_card(player3, center_pile, turn_controller, challenge_controller)
                    is_game_over = check_for_game_over(challenge_controller)
                if pressed_keys[pygame.K_p]:
                    board_controller.hand_slap(3)
                    slap(player3, center_pile, turn_controller, challenge_controller)
                    is_game_over = check_for_game_over(challenge_controller)
                if pressed_keys[pygame.K_SPACE]:
                    print('Centerpile.cards:', center_pile.cards)
                    print('player1:', player1.deck)
                    print('player2:', player2.deck)
                    print('player3:', player3.deck)
                    print('current_turn:', turn_controller.current_turn)
                    print("player1",player1.is_playing)
                    print("player2",player2.is_playing)
                    print("player3",player3.is_playing)

        #------------out of for loop--------------------------------------------------------------------out of for event loop
        if card_delay > 0:
            card_delay -= 1

        if challenge_controller.delay_challenge_loss > 0:
            challenge_controller.delay_challenge_loss -= 1

        elif challenge_controller.delay_challenge_loss == 0:
            challenge_controller.resolve_lost_challenge()

        board_controller.set_up_board(center_pile.cards, [len(player1.deck), len(player2.deck), len(player3.deck)],turn_controller.current_turn,challenge_controller.tries)

        if not is_game_over:
            pygame.display.update()
        else:
            if not has_displayed_game_over:
                #has_displayed_game_over = True
                if player1.is_playing == True:
                    board_controller.game_over_screen(1)
                if player2.is_playing == True:
                    board_controller.game_over_screen(2)
                if player3.is_playing == True:
                    board_controller.game_over_screen(3)
                pygame.display.update()
                #TODO display game over here!
                #print('game over')
            if pressed_keys[pygame.K_SPACE]:
                new_game(player1,player2,player3,center_pile,challenge_controller)
                is_game_over = False
                has_displayed_game_over = False
                board_controller.moveing_x = 0
                board_controller.moveing_y = 0

main()