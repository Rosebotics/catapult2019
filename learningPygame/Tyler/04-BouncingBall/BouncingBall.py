import pygame
import sys


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
        if self.x > 300 - self.radius or self.x < 0 + self.radius:
            self.speed_x *= -1

        if self.y > 300 - self.radius or self.y < 0 + self.radius:
            self.speed_y *= -1
        self.x += self.speed_x
        self.y += self.speed_y

    # def hit_wall(self, raindrop):
    #     return pygame.Rect(self.x, self.y, , 192).collidepoint(raindrop.x, raindrop.y)





def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class

    ball = Ball(screen, (0, 255, 0), 100, 100, 10, 5, 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))




        # TODO: Move the ball
        ball.move()

        # TODO: Draw the ball
        ball.draw()

        pygame.display.update()


main()
