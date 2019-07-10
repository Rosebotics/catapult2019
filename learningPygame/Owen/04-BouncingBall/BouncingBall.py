import pygame
import sys
import random


# DONE: Create a Ball class.
class Ball:
# DONE: Member variables: screen, color, x, y, radius, speed_x, speed_y
    def __init__(self, screen, x, y, color):
        self.screen = screen
        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.circle_radius = 4
        self.speed_x = 9
        self.speed_y = 10
        self.color = color

    def move(self):
        self.y = self.y + self.speed_y
        self.x = self.x + self.speed_x
        if self.x > 296 or self.x < 4:
            self.speed_x = -self.speed_x
        if self.y > 296 or self.y < 4:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 8, 8)

# DONE: Methods __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # DONE: Create an instance of the Ball class
    myball = Ball(screen, 40, 90, (80, 180, 50))
    balls = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                new_ball = Ball(screen, random.randint(0, 300), random.randint(0, 300), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
                balls.append(new_ball)
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        myball.move()
        # TODO: Draw the ball
        myball.draw()

        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()

main()