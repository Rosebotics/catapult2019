import pygame
import sys
import random
random.seed()
# DONE: Create a Ball class.
# DONE: Member variables: screen, color, x, y, radius, speed_x, speed_y
# DONE: Methods __init__, draw, move
class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.xspeed = speed_x
        self.yspeed = speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        if self.x < self.radius or self.x > 300 - self.radius:
            self.xspeed *= -1
            self.x += (self.xspeed * 2)
        if self.y < self.radius or self.y > 300-self.radius:
            self.yspeed *= -1
            self.y += (self.yspeed * 2)
        self.x += self.xspeed
        self.y += self.yspeed


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    # DONE: Create an instance of the Ball class
    balls = []
    for i in range(random.randint(1, 300)):
        colorr = random.randint(0, 255)
        colorg = random.randint(0, 255)
        colorb = random.randint(0, 255)
        size = random.randint(10, 20)
        xpos = random.randint(50, 250)
        ypos = random.randint(50, 250)
        xspeed = random.randint(-5, 5)
        yspeed = random.randint(-5, 5)
        if xspeed == 0:
            xspeed = 5
        if yspeed == 0:
            yspeed = 5
        balls.append(Ball(screen, (colorr, colorg, colorb), xpos, ypos, size, xspeed, yspeed))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        for ball in balls:
            ball.move()
        # TODO: Draw the ball
        for ball in balls:
            ball.draw()
        pygame.display.update()


main()
