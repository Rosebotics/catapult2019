import pygame
import sys
import random

# Done: Create a Ball class.
# ASK: Member variables: screen, color, x, y, radius, speed_x, speed_y
# Done: Methods __init__, draw, move
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = random.randint(1, 15)
        self.speed_y = random.randint(1, 15)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 15)

    def move(self):
        self.y = self.y + self.speed_y
        self.x = self.x + self.speed_x

        if self.x >= 400 or self.x <= 0:
            self.speed_x = -self.speed_x
        if self.y >= 400 or self.y <= 0:
            self.speed_y = -self.speed_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # Done: Create an instance of the Ball class
    # ball = Ball(screen, 45, 120)

    ball_list = []
    for x in range(20):
        new_ball = Ball(screen, random.randint(50, 250), random.randint(50, 250))
        ball_list.append(new_ball)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # # Done: Move the ball
        # ball.move()
        #
        # # Done: Draw the ball
        # ball.draw()

        for ball in ball_list:
            ball.move()
            ball.draw()

        pygame.display.update()


main()
