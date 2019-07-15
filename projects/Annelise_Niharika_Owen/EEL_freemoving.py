import pygame, sys, random, time


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
class Game:
    def __init__(self, screen, clock, scoreboard, gameover_image2, level1_image):
        self.screen = screen
        self.clock = clock
        self.scoreboard = scoreboard
        self.level1_image = level1_image
        self.gameover_image2 = gameover_image2
        self.starfish = Starfish(self.screen, 10, 35)
        self.pearl_fleet = PearlFleet(self.screen)
        self.waterbottles = self.create_waterbottles()
        self.sodas = self.create_sodas()

    def create_waterbottles(self):
        waterbottles = []
        number_of_waterbottles_in_region_1 = random.randint(5, 10)

        for x in range(number_of_waterbottles_in_region_1):
            waterbottle = WaterBottle(self.screen, random.randint(0, 80), random.randint(55, 900))
            waterbottles.append(waterbottle)

        number_of_waterbottles_in_region_2 = 50 - number_of_waterbottles_in_region_1

        for x in range(number_of_waterbottles_in_region_2):
            waterbottle = WaterBottle(self.screen, random.randint(90, 900), random.randint(0, 900))
            waterbottles.append(waterbottle)
        return waterbottles

    def create_sodas(self):
        sodas=[]
        number_of_sodas_in_region_1 = 4
        for x in range(number_of_sodas_in_region_1):
            soda = Soda(self.screen, random.randint(0, 80), random.randint(55, 900))
            sodas.append(soda)
        return sodas

    def reset_game(self):
        self.starfish = Starfish(self.screen, 10, 35)
        self.pearl_fleet = PearlFleet(self.screen)
        self.waterbottles = self.create_waterbottles()
        self.sodas = self.create_sodas()
        self.scoreboard.score = 0

    def run(self):
        is_game_over = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            if not is_game_over:
                # Check for game key presses
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    self.starfish.y = self.starfish.y - 5
                if pressed_keys[pygame.K_DOWN]:
                    self.starfish.y = self.starfish.y + 5
                if pressed_keys[pygame.K_LEFT]:
                    self.starfish.x = self.starfish.x - 5
                if pressed_keys[pygame.K_RIGHT]:
                    self.starfish.x = self.starfish.x + 5
                if pressed_keys[pygame.K_SPACE] and is_game_over:
                    self.reset_game()
                    self.run()

                # Check if the game is over
                for waterbottle in self.waterbottles:
                    if waterbottle.hit_by(self.starfish):
                        print("A waterbottle is hitting a starfish")
                        is_game_over = True


            for pearl in self.pearl_fleet.pearls:
                if pearl.hit_by(self.starfish):
                    pearl.collected = True
                    self.scoreboard.score = self.scoreboard.score + 5
                    self.pearl_fleet.remove_collected_pearls()

            for waterbottle in self.waterbottles:
                waterbottle.draw()

            for soda in self.sodas:
                soda.move()
                soda.draw()

            for pearl in self.pearl_fleet.pearls:
                pearl.draw()
            self.starfish.move()
            self.starfish.draw()
            self.scoreboard.draw()

            self.screen.blit(self.level1_image, (0, 0))

            if is_game_over:
                print("I'm about to blit the game over image")
                self.screen.blit(self.gameover_image2, (0, 0))

            pygame.display.update()
            self.clock.tick(60)


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
        elif self.y < -60:
            self.y = 850

class Pearl:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('pearl.png')
        self.collected = False

        # self.rect = self.image.get_rect()
        # self.rect[0] = self.x
        # self.rect[1] = self.y

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, starfish):
        return pygame.Rect(self.x, self.y, 40, 30).collidepoint(starfish.x + 33.5, starfish.y + 25)

class PearlFleet:
    def __init__(self, screen):
        # Already done.  Prepares the list of Badguys.
        self.pearls = []
        for x in range(3):
            pearl = Pearl(screen, random.randint(60, 850), random.randint(20, 850))
            self.pearls.append(pearl)

    def remove_collected_pearls(self):
        for k in range(len(self.pearls) - 1, -1, -1):
            if self.pearls[k].collected:
                del self.pearls[k]


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

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("STARFISH!")
    screen = pygame.display.set_mode((900, 900))
    gameover_image2 = pygame.image.load('gameover_image2.png')
    level1_image = pygame.image.load('level_1.png')

    scoreboard = Scoreboard(screen)
    game = Game(screen, clock, scoreboard, gameover_image2, level1_image)

    game.run()



main()