import pygame
import sys
import random


# TODO: Create a Ball class.
# TODO: Member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods __init__, draw, move

class Ball:

    def __init__(self, screen):
        self.screen = screen
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = random.randint(0, screen.get_width())
        self.y = random.randint(0, screen.get_height())
        self.radius = random.randint(0, 35)
        self.speed_x = random.randint(0, 10)
        self.speed_y = random.randint(0, 10)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.collision()
        self.x += self.speed_x
        self.y += self.speed_y

    def collision(self):
        if self.x + (self.radius * 2) + self.speed_x > self.screen.get_width():
            self.speed_x *= -1
        if self.x + self.speed_x < 0:
            self.speed_x *= -1
        if self.y + (self.radius * 2) + self.speed_y > self.screen.get_height():
            self.speed_y *= -1
        if self.y + self.speed_y < 0:
            self.speed_y *= -1

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class
    balls = []

    for i in range(random.randint(0, 50)):
        balls.append(Ball(screen))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        # TODO: Draw the ball
        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()
