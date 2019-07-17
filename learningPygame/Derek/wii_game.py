import pygame, random, time

def make_possible_button_objects():
    possible_buttons = []

    button_location = (50, 300)

    possible_buttons.append(GameAction('A', button_location, pygame.image.load('A.png')))
    # possible_buttons.append(GameAction('B', button_location, pygame.image.load('B.png')))
    # possible_buttons.append(GameAction('Up', button_location, pygame.image.load('up_arrow.png')))
    # possible_buttons.append(GameAction('Down', button_location, pygame.image.load('down_arrow.png')))
    # possible_buttons.append(GameAction('Left', button_location, pygame.image.load('left_arrow.png')))
    # possible_buttons.append(GameAction('Right', button_location, pygame.image.load('right_arrow.png')))

    return possible_buttons

def make_possible_turn_objects():
    possible_turns = []

    turn_location = (300, 300)

    possible_turns.append(GameAction('Rotate Left', turn_location, pygame.image.load('rotate_left.png')))
    possible_turns.append(GameAction('Rotate Right', turn_location, pygame.image.load('rotate_right.png')))
    possible_turns.append(GameAction('Rotate Up', turn_location, pygame.image.load('up_arrow.png')))
    possible_turns.append(GameAction('Rotate Down', turn_location, pygame.image.load('down_arrow.png')))

    return possible_turns

class GameAction:
    def __init__(self, name, location, image):
        self.name = name
        self.location = location
        self.image = image

    def draw(self, frame):
        frame.blit(self.image, self.location)

class CombinationMaker:
    def __init__(self, possible_buttons, possible_turns):
        self.possible_buttons = possible_buttons
        self.possible_turns = possible_turns

    def get_random_combination(self):
        button = self.possible_buttons[random.randint(0, len(self.possible_buttons) - 1)]
        turn = self.possible_turns[random.randint(0, len(self.possible_turns) - 1)]

        return button, turn

class Frame:
    def __init__(self):
        self.frame = pygame.display.set_mode((500, 500))
        self.fill_color = (0, 0, 0)

    def set_fill_color(self, color):
        self.fill_color = color

    def update(self, game_action_combination, display_time):
        self.frame.fill(self.fill_color)

        font = pygame.font.Font(None, 30)

        time_remaining_surface = font.render("Time Remaining: " + str(display_time), True, (255, 255, 255))

        self.frame.blit(time_remaining_surface, (50, 50))

        self.frame.blit(game_action_combination[0].image, game_action_combination[0].location)
        self.frame.blit(game_action_combination[1].image, game_action_combination[1].location)
        pygame.display.update()

class Game:
    def __init__(self, frame, combination_maker, wii_remote):
        self.frame = frame
        self.combination_maker = combination_maker
        self.wii_remote = wii_remote
        self.current_combination = None
        self.current_combination_deploy_time = None
        self.combination_response_threshold = 3

    def run(self):
        playing_wii_game = True

        user_played_correctly = False

        while playing_wii_game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing_wii_game = False
                if event.type == pygame.JOYBUTTONDOWN:
                    if self.current_combination != None:
                        if event.button == 2:
                            if self.current_combination[1].name == 'Rotate Left':
                                if self.wii_remote.get_axis(4) > 0.15:
                                    user_played_correctly = True
                                else:
                                    user_played_correctly = False

                            if self.current_combination[1].name == 'Rotate Right':
                                if self.wii_remote.get_axis(4) < -0.15:
                                    user_played_correctly = True
                                else:
                                    user_played_correctly = False

                            if self.current_combination[1].name == 'Rotate Up':
                                if self.wii_remote.get_axis(5) > 0.15:
                                    user_played_correctly = True
                                else:
                                    user_played_correctly = False

                            if self.current_combination[1].name == 'Rotate Down':
                                if self.wii_remote.get_axis(5) < -0.15:
                                    user_played_correctly = True
                                else:
                                    user_played_correctly = False

            if self.current_combination == None:
                current_button, current_turn = self.combination_maker.get_random_combination()
                self.current_combination_deploy_time = time.time()
                self.current_combination = (current_button, current_turn)

            if user_played_correctly:
                self.frame.set_fill_color(pygame.Color('green'))
                self.frame.update(self.current_combination, 3 - (time.time() - self.current_combination_deploy_time))
                self.current_combination = None
                user_played_correctly = False
            else:
                if self.current_combination_is_timed_out(time.time()):
                    self.frame.set_fill_color(pygame.Color('red'))
                    self.current_combination = None
                else:
                    self.frame.update(self.current_combination, 3 - (time.time() - self.current_combination_deploy_time))

    def current_combination_is_timed_out(self, current_time):
        return current_time - self.current_combination_deploy_time > self.combination_response_threshold


def main():
    pygame.init()

    frame = Frame()

    combination_maker = CombinationMaker(make_possible_button_objects(), make_possible_turn_objects())

    try:
        wii_remote = pygame.joystick.Joystick(0)
        wii_remote.init()
    except pygame.error:
        wii_remote = None

    if wii_remote is not None:
        game = Game(frame, combination_maker, wii_remote)
        game.run()
    else:
        print('Unable to connect to Wii Remote')


main()