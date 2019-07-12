import pygame, sys, random, time

class WaterBottle:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('water_bottle.png')

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Starfish:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('starfish.png')

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

    starfish =

    waterbottles = []
    for x in range(50):
        waterbottle = WaterBottle(screen, random.randint(60, 850), random.randint(60, 850))
        waterbottles.append(waterbottle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(level1_image, (0, 0))
        for waterbottle in waterbottles:
            waterbottle.draw()

        starfish.draw()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            starfish.y = starfish.y - 5



        clock.tick(60)
        pygame.display.update()

main()