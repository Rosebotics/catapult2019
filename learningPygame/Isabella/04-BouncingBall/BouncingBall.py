import pygame
import sys
import time
import random

class Ball:
# TODO: Create a Ball class.
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_y = random.randint(1, 5)
        self.speed_x = random.randint(1, 5)

    def move(self):
        self.y = self.y + self.speed_y
        self.x = self.x + self.speed_x
        if self.x > 285:
            self.speed_x = -1*self.speed_x
        if self.y > 285:
            self.speed_y = -1*self.speed_y
        if self.y < 15:
            self.speed_y = -1*self.speed_y
        if self.x < 15:
            self.speed_x = -1*self.speed_x
    def draw(self):
        pygame.draw.circle(self.screen, (255, 167, 180), (self.x, self.y), 15)
# TODO: Member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill((0, 255, 255))
    clock = pygame.time.Clock()
    ball = []
    for i in range(random.randint(5, 1000)):
        ball.append(Ball(screen, 25, 25))
    # TODO: Create an instance of the Ball class

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill((0, 255, 255))

        # TODO: Move the ball
        for bass in ball:
            bass.move()
        # TODO: Draw the ball
            bass.draw()
        pygame.display.update()




main()
