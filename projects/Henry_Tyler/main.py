import pygame, sys, random, time

class Player:
    def __init__(self, screen, column, direction, color):
        self.screen = screen
        self.x = 125
        self.y = 800
        self.column = column
        self.direction = direction
        self.color = color

    def draw(self):
        #pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x+50, self.y-20), (self.x + 100, self.y), (self.x + 100, self.y +50), (self.x + 50, self.y +30), (self.x, self.y +50)])
        pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 66), (self.x + 75, self.y - 100), (self.x + 150, self.y - 66), (self.x + 150, self.y), (self.x + 75, self.y - 33)], 1)
    def move(self):
        pass


class Enemy:
    def __init__(self, screen, column, direction, color, y, speed):
        self.screen = screen
        self.column = column
        self.direction = direction
        self.color = color
        self.y = y
        self.speed = speed
        self.is_hit = False

class EnemyList:
    def __init__(self, screen):
        self.screen = screen
        self.enemy_list = []

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.x = 10
        self.y = 10
        self.score = 0

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("cool gaem")
    screen = pygame.display.set_mode((400, 800))
    player = Player(screen, 1, False, (255, 0, 0))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(pygame.Color("Black"))
        player.draw()
        pygame.display.update()

main()