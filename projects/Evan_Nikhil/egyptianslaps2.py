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

    def add_card(self, new_card):
        self.cards.append(new_card)
        self.is_slap_allowed = False
        if len(self.cards) > 1:
            if self.cards[-1] == self.cards[-2]:
                self.is_slap_allowed = True

        if len(self.cards) > 2:
            if self.cards[-1] == self.cards[-3]:
                self.is_slap_allowed = True
        print(self.cards)

    def bury_card(self, new_card):
        self.cards.insert(0, new_card)
        print(self.cards)

    def get_top_card(self):
        if len(self.cards) > 0:
            return self.cards[-1]


class TurnController:
    def __init__(self, player1, player2, player3):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.previous_turn = -1
        self.current_turn = 1

    def set_turn_to(self, new_player_turn):
        self.previous_turn = self.current_turn
        self.current_turn = new_player_turn

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


    def possible_challenge(self):
        # assumes a card has just been played and there is no active challenge it moves on to the next player.
        top_card = self.center_pile.get_top_card()
        is_new_challenge = False
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
        if top_card == 'J' or top_card == 'Q' or top_card == 'K' or top_card == 'A':
            self.is_challenge_active = False
            self.possible_challenge()
        else:
            self.tries = self.tries - 1
            if self.tries == 0:
                self.challenger.deck = self.challenger.deck + self.center_pile.cards
                self.center_pile.cards = []
                self.turn_controller.set_turn_to(self.challenger.player_number)
                self.is_challenge_active = False
            elif not self.challengee.is_playing:
                print('challengee ran out of cards')
                self.turn_controller.next_turn()
                self.challengee = self.turn_controller.get_current_player()

        # print('after')
        # print("   self.is_challenge_active", self.is_challenge_active)
        # print("   self.tries", self.tries)
        # print("   self.challenger.player_number", self.challenger.player_number)
        # print("   self.challengee.player_number", self.challengee.player_number)

    # TODO Consider giving people a chance to slap while challenge is going on.


# #----------------------------------------------------------------------------- functions

def slap(player, center_pile, turn_controller, challenge_controller):
    if not player.is_playing:
        if not (challenge_controller.is_challenge_active and challenge_controller.challenger.player_number == player.player_number):
            return
    if center_pile.is_slap_allowed:
        player.deck = player.deck + center_pile.cards
        center_pile.cards = []
        turn_controller.set_turn_to(player.player_number)
        print(center_pile.cards)
    else:
        if len(center_pile.cards) > 1 and player.is_playing:
            player.discard_card(center_pile)


def play_card(player, center_pile, turn_controller, challenge_controller):
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


    #-----------------------------------------------------------------------------------------------------------
    is_game_over = False
    has_displayed_game_over = False

    while True:
        clock.tick(60)
        pressed_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if pressed_keys[pygame.K_BACKQUOTE]:
                play_card(player1, center_pile, turn_controller, challenge_controller)
                is_game_over = check_for_game_over(challenge_controller)
            if pressed_keys[pygame.K_1]:
                slap(player1, center_pile, turn_controller, challenge_controller)
                is_game_over = check_for_game_over(challenge_controller)
            if pressed_keys[pygame.K_v]:
                play_card(player2, center_pile, turn_controller, challenge_controller)
                is_game_over = check_for_game_over(challenge_controller)
            if pressed_keys[pygame.K_b]:
                slap(player2, center_pile, turn_controller, challenge_controller)
                is_game_over = check_for_game_over(challenge_controller)
            if pressed_keys[pygame.K_o]:
                play_card(player3, center_pile, turn_controller, challenge_controller)
                is_game_over = check_for_game_over(challenge_controller)
            if pressed_keys[pygame.K_p]:
                slap(player3, center_pile, turn_controller, challenge_controller)
                is_game_over = check_for_game_over(challenge_controller)
            if pressed_keys[pygame.K_SPACE]:
                print('Centerpile.cards:', center_pile.cards)
                print('player1:', player1.deck)
                print('player2:', player2.deck)
                print('player3:', player3.deck)
                print('current_turn:', turn_controller.current_turn)

        #------------out of for loop--------------------------------------------------------------------out of for event loop
        screen.fill((220, 181, 121))
        if not is_game_over:
            pygame.display.update()
        else:
            if not has_displayed_game_over:
                has_displayed_game_over = True
                #TODO display game over here!
                print('game over')

main()