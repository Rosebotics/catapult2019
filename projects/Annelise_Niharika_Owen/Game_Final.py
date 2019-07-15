import pygame, sys, random, time, math
from pygame.locals import *


class WaterBottle:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('water_bottle.png')

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, starfish):
        return pygame.Rect(self.x, self.y, 40, 50).collidepoint(starfish.x + 33.5, starfish.y + 25)


class Soda:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.x_speed = random.randint(-10, 10)
        self.y_speed = random.randint(-10, 10)
        if self.x_speed == 0:
            self.x_speed = 2
        if self.y_speed == 0:
            self.y_speed = 2
        self.image = pygame.image.load('soda.png')

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        if self.x > 900:
            self.x = -50
        elif self.x < -60:
            self.x = 850

        if self.y > 900:
            self.y = -50
        elif self.y < -60:
            self.y = 850

    def hit_by(self, starfish):
        return pygame.Rect(self.x, self.y, 40, 50).collidepoint(starfish.x + 33.5, starfish.y + 25)


class Starfish:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('starfish.png')
        # self.dead = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.x > 900:
            self.x = -50
        elif self.x < -60:
            self.x = 850

        if self.y > 900:
            self.y = -50
        elif self.y < -60: # DAWGG, YUR HI KEE DUM NUDDY LITT WIT IT'
            self.y = 850


class Pearl:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('pearl.png')
        self.collected = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, starfish):
        return pygame.Rect(self.x, self.y, 40, 30).collidepoint(starfish.x + 33.5, starfish.y + 25)


class PearlFleet:
    def __init__(self, screen):
        self.screen = screen
        self.pearls = []
        for x in range(3):
            pearl = Pearl(screen, random.randint(60, 850), random.randint(20, 850))
            self.pearls.append(pearl)

    def remove_collected_pearls(self):
        for k in range(len(self.pearls) - 1, -1, -1):
            if self.pearls[k].collected:
                del self.pearls[k]

    def add_pearls(self):
        pearl = Pearl(self.screen, random.randint(60, 850), random.randint(20, 850))
        self.pearls.append(pearl)


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.x = 5
        self.y = 5
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        text_as_image = self.font.render("Score: " + str(self.score), True, (255, 255, 255), (0, 0, 0))
        self.screen.blit(text_as_image, (5, 5))


class Countdown:
    def __init__(self, screen):
        self.screen = screen
        self.x = 690
        self.y = 5
        self.font = pygame.font.Font(None, 30)

    def draw(self, countdown_time):
        text_as_image = self.font.render("Remaining Time: " + str(countdown_time), True, (255, 255, 255), (0, 0, 0))
        self.screen.blit(text_as_image, (self.x, self.y))


def main():
    pygame.init()
    pygame.font.init()
    caption_font = pygame.font.Font(None, 100)
    clock = pygame.time.Clock()
    pygame.display.set_caption("STARFISH!")
    screen = pygame.display.set_mode((900, 900))
    gameover_image2 = pygame.image.load('gameover_image2.png')
    level1_image = pygame.image.load('level_1.png')
    gamewin = pygame.image.load('gamewin.png')

    scoreboard = Scoreboard(screen)

    countdown = Countdown(screen)

    is_game_over = False

    starfish = Starfish(screen, 10, 35)

    pearl_fleet = PearlFleet(screen)

    waterbottles = []
    number_of_waterbottles_in_region_1 = random.randint(5, 10)

    for x in range(number_of_waterbottles_in_region_1):
        waterbottle = WaterBottle(screen, random.randint(0, 80), random.randint(55, 900))
        waterbottles.append(waterbottle)

    number_of_waterbottles_in_region_2 = 50 - number_of_waterbottles_in_region_1

    for x in range(number_of_waterbottles_in_region_2):
        waterbottle = WaterBottle(screen, random.randint(90, 900), random.randint(0, 900))
        waterbottles.append(waterbottle)

    sodas = []
    number_of_sodas_in_region_1 = 4

    for x in range(number_of_sodas_in_region_1):
        soda = Soda(screen, random.randint(0, 80), random.randint(55, 900))
        sodas.append(soda)

    background_sound = pygame.mixer.Sound("water_background.wav")
    background_sound.play(-1)

    pearl_sound = pygame.mixer.Sound("pearl.wav")
    soda_sound = pygame.mixer.Sound("sodacan.wav")
    waterbottle_sound = pygame.mixer.Sound("bottle.wav")

    starting_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(level1_image, (0, 0))

        if not is_game_over:
            # Check for game key presses
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                starfish.y = starfish.y - 5
            if pressed_keys[pygame.K_DOWN]:
                starfish.y = starfish.y + 5
            if pressed_keys[pygame.K_LEFT]:
                starfish.x = starfish.x - 5
            if pressed_keys[pygame.K_RIGHT]:
                starfish.x = starfish.x + 5
            # Check if the game is over
            for waterbottle in waterbottles:
                if waterbottle.hit_by(starfish):
                    waterbottle_sound.play()
                    is_game_over = True

            for soda in sodas:
                if soda.hit_by(starfish):
                    soda_sound.play()
                    is_game_over = True

        for pearl in pearl_fleet.pearls:
            if pearl.hit_by(starfish):
                pearl_sound.play()
                pearl.collected = True
                scoreboard.score = scoreboard.score + 5
                pearl_fleet.remove_collected_pearls()
                pearl_fleet.add_pearls()


        for waterbottle in waterbottles:
            waterbottle.draw()

        for soda in sodas:
            soda.move()
            soda.draw()

        for pearl in pearl_fleet.pearls:
            pearl.draw()
        starfish.move()
        starfish.draw()
        scoreboard.draw()
        score_display = caption_font.render("Score: " + str(scoreboard.score), True, (255, 255, 255))

        if is_game_over:
            screen.blit(gameover_image2, (0, 0))
            screen.blit(score_display, (330, 800))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            main()

        current_time = time.time()
        game_time = current_time - starting_time

        if game_time >= 120:
            is_game_over = True
            screen.blit(gamewin, (0, 0))

        countdown_time = 120 - game_time
        if not is_game_over:
            countdown.draw(math.floor(countdown_time))


        pygame.display.update()
        clock.tick(60)


main()