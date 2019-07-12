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


class Eel:
    def __init__(self, screen, x, y, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('eel.png')
        pass

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

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

# class Scoreboard:
#     def __init__(self):



def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("EEL!")
    screen = pygame.display.set_mode((900, 900))
    gameover_image2 = pygame.image.load('gameover_image2.png')
    level1_image = pygame.image.load('level_1.png')
    score = 0

    is_game_over = False

    starfish = Starfish(screen, 50, 60)

    pearl_fleet = PearlFleet(screen)

    waterbottles = []
    for x in range(50):
        waterbottle = WaterBottle(screen, random.randint(70, 850), random.randint(20, 850))
        waterbottles.append(waterbottle)

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
                    is_game_over = True

        for pearl in pearl_fleet.pearls:
            if pearl.hit_by(starfish):
                pearl.collected = True
                pearl_fleet.remove_collected_pearls()

        for waterbottle in waterbottles:
            waterbottle.draw()

        for pearl in pearl_fleet.pearls:
            pearl.draw()
        starfish.move()
        starfish.draw()

        if is_game_over:
            screen.blit(gameover_image2, (0, 0))

        pygame.display.update()
        clock.tick(60)


main()