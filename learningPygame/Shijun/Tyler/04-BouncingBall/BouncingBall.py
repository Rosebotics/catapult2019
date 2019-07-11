import pygame
import sys
import random


# TODO: Create a Ball class.
# TODO: Member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods __init__, draw, move

class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        if self.x > self.screen.get_width() - self.radius or self.x < 0 + self.radius:
            self.speed_x *= -1

        if self.y > self.screen.get_height() - self.radius or self.y < 0 + self.radius:
            self.speed_y *= -1
        self.x += self.speed_x
        self.y += self.speed_y

    # def hit_wall(self, raindrop):
    #     return pygame.Rect(self.x, self.y, , 192).collidepoint(raindrop.x, raindrop.y)



def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class

    #ball = Ball(screen, (0, 255, 0), 100, 100, 10, 5, 3)

    balls = []
    for k in range(1000):
        radius = random.randint(3, 10)
        new_ball = Ball(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(20, screen.get_width()), random.randint(20, screen.get_height()), radius, random.randint(-5, 5), random.randint(-5, 5))
        balls.append(new_ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))




        # TODO: Move the ball
        #ball.move()

        # TODO: Draw the ball
        #ball.draw()

        for ball in balls:
            ball.move()
            ball.draw()


        pygame.display.update()


main()
