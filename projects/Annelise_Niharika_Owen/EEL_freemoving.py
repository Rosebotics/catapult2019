import pygame, sys, random, time

class WaterBottle:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('water_bottle.png')

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Head:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self.screen, (255, 165, 0), (self.x, self.y), 5)

    def move(self):
        pass

class Fish:
    pass

class Scoreboard:
    pass

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("EEL!")
    screen = pygame.display.set_mode((900, 900))
    level1_image = pygame.image.load('level_1.png')

    # level1_image = pygame.transform.scale(level1_image, (IMAGE_SIZE, IMAGE_SIZE))

    waterbottles = []

    for x in range(6):
        waterbottle = WaterBottle(screen, random.randint(20, 850), random.randint(20, 850))
        waterbottles.append(waterbottle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(level1_image, (0, 0))
        for waterbottle in waterbottles:
            waterbottle.draw()

        clock.tick(60)
        pygame.display.update()

main()