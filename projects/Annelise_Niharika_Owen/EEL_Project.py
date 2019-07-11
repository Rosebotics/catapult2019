import pygame, sys, random, time

class WaterBottle:
    pass


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

class Body:
    pass

class Scoreboard:
    pass

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("EEL!")
    screen = pygame.display.set_mode((1000, 1000))
    level1_image = pygame.image.load('level_1.png')
    screen.blit(level1_image, (0,0))
    # level1_image = pygame.transform.scale(level1_image, (IMAGE_SIZE, IMAGE_SIZE))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    clock.tick(60)
    pygame.display.update()\

main()