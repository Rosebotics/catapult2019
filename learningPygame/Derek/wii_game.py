import pygame, random, time

def make_possible_button_objects():
    possible_buttons = []

    button_location = (50, 300)

    possible_buttons.append(GameAction('A', button_location, pygame.image.load('A.png')))
    possible_buttons.append(GameAction('B', button_location, pygame.image.load('B.png')))
    possible_buttons.append(GameAction('Up', button_location, pygame.image.load('up_arrow.png')))
    possible_buttons.append(GameAction('Down', button_location, pygame.image.load('down_arrow.png')))
    possible_buttons.append(GameAction('Left', button_location, pygame.image.load('left_arrow.png')))
    possible_buttons.append(GameAction('Right', button_location, pygame.image.load('right_arrow.png')))

    return possible_buttons

def make_possible_turn_objects():
    possible_turns = []

    turn_location = (300, 300)

    possible_turns.append(GameAction('Rotate Left', turn_location, pygame.image.load('rotate_left.png')))
    possible_turns.append(GameAction('Rotate Right', turn_location, pygame.image.load('rotate_right.png')))

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

class GameActionChecker:
    def __init__(self, wii_remote):
        self.wii_remote = wii_remote

        self.button_numbers_to_button_names = {
            0: lambda button_press_name : button_press_name == "A",
            1: lambda button_press_name : button_press_name == "B",
            "Up": round(self.wii_remote.get_axis(0)) == -1,
            "Down": round(self.wii_remote.get_axis(0)) == 1,
            "Left": round(self.wii_remote.get_axis(1)) == -1,
            "Right": round(self.wii_remote.get_axis(1)) == 1
        }

        self.buttons_and_turns_to_checker_functions = {}

    def check_game_action_combination(self, user_action_information):
        # TODO: Fill in with successful move logic
        if user_action_information.correct_button.name == 'A' or user_action_information.correct_button.name == 'B':
            if self.button_numbers_to_button_names[user_action_information.button_press]()


        correct_button_press = self.button_numbers_to_button_names[user_action_information.button_press]
        if buttonbutton_pressed_name != user_action_information.correct_button.name:
            return False
        elif
        else:
            self.correct



        pass

class UserActionWrapper:
    def __init__(self, correct_button, correct_turn, button_press, axis_0, axis_1, axis_4):
        self.correct_button = correct_button
        self.correct_turn = correct_turn
        self.button_press = button_press
        self.axis_0 = axis_0
        self.axis_1 = axis_1
        self.axis_4 = axis_4

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

        print("Button is: " + game_action_combination[0].name)
        print("Turn is: " + game_action_combination[1].name)

        self.frame.blit(game_action_combination[0].image, game_action_combination[0].location)
        self.frame.blit(game_action_combination[1].image, game_action_combination[1].location)
        pygame.display.update()

class Game:
    def __init__(self, frame, combination_maker, valid_combination_checker, wii_remote):
        self.frame = frame
        self.combination_maker = combination_maker
        self.valid_combination_checker = valid_combination_checker
        self.wii_remote = wii_remote
        self.current_combination = None
        self.current_combination_deploy_time = None
        self.combination_response_threshold = 3

    def run(self):
        playing_wii_game = True

        while playing_wii_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing_wii_game = False
                if event.type == pygame.JOYBUTTONDOWN:
                    if self.current_combination != None:
                        user_action = \
                            UserActionWrapper(self.current_combination[0], self.current_combination[1], event.button,
                                              self.wii_remote.get_axis(0), self.wii_remote.get_axis(1), self.wii_remote.get_axis(4))
                        correct_button_press = self.valid_combination_checker.check_game_action_combination(user_action)
                        if correct_button_press:
                            self.valid_combination_checker.check_game_action_button(event.button)

            if self.current_combination == None:
                current_button, current_turn = self.combination_maker.get_random_combination()
                self.current_combination_deploy_time = time.time()
                self.current_combination = (current_button, current_turn)
            else:
                if self.current_combination_is_timed_out(time.time()):
                    self.current_combination = None
                    self.frame.set_fill_color(pygame.Color('red'))
                elif self.valid_combination_checker.check_game_action_combination(current_button, current_turn):
                    self.frame.set_fill_color(pygame.Color('green'))
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

    if wii_remote.wii_remote is not None:
        valid_combination_checker = GameActionChecker(wii_remote)
        game = Game(frame, combination_maker, valid_combination_checker, wii_remote)
        game.run()
    else:
        print('Unable to connect to Wii Remote')






main()