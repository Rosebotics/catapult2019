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

class Board:
    def __init__(self):
        self.board = [['.' for _ in range(25)] for _ in range(25)]

    def check_for_game_over(self):
        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])

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

    for x in range(60):
        waterbottle = WaterBottle(screen, random.randint(50, 850), random.randint(50, 850))
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