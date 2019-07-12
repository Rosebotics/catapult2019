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
        return pygame.Rect(self.x, self.y, 67, 50).collidepoint(starfish.x, starfish.y)

class Starfish:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('starfish.png')
        self.dead = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class Eel:
    def __init__(self, screen, x, y, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('eel.png')

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class Pearl:
    def __init__(self, screen, x, y, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('pearl.png')
        self.rect = self.image.get_rect()
        self.rect[0] = self.x
        self.rect[1] = self.y


    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Scoreboard:
    pass

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("EEL!")
    screen = pygame.display.set_mode((900, 900))
    level1_image = pygame.image.load('level_1.png')

    is_game_over = False

    starfish = Starfish(screen, 55, 60)

    pearls = []
    for x in range(3):
        pearl = Pearl(screen, random.randint(60, 850), random.randint(60, 850))
        # pearls.append(pearl)


    waterbottles = []
    for x in range(50):
        waterbottle = WaterBottle(screen, random.randint(60, 850), random.randint(60, 850))
        waterbottles.append(waterbottle)

    # .collidepoint

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(level1_image, (0, 0))
        for waterbottle in waterbottles:
            waterbottle.draw()
        for pearl in pearls:
            pearl.draw()

        starfish.draw()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            starfish.y = starfish.y - 5
        if pressed_keys[pygame.K_DOWN]:
            starfish.y = starfish.y + 5
        if pressed_keys[pygame.K_LEFT]:
            starfish.x = starfish.x - 5
        if pressed_keys[pygame.K_RIGHT]:
            starfish.x = starfish.x + 5

        for waterbottle in waterbottles:
            if waterbottle.hit_by(starfish):
                starfish.dead = True
                is_game_over = True
            # TODO: Define dead

        clock.tick(60)
        if not is_game_over:
            pygame.display.update()

            for waterbottle in waterbottles:
                if waterbottle.hit_by(starfish) = True:
                    screen.blit(gameover_image, (450, 450))
                    pygame.display.update()
                    is_game_over = True

main()