import pygame
import sys


# TODO: Create a Ball class.

class Ball:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.radius = 5

# TODO: Member variables: screen, color, x, y, radius, speed_x, speed_y




# TODO: Methods __init__, draw, move

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), self.radius)

    def move(self):
        if self.speed_x + 2 * self.radius + self.x > self.screen.get_width():
           self.speed_x = self.speed_x * -1

        if self.speed_x + self.x < 0:
           self.speed_x = self.speed_x * -1

        if self.speed_y + self.y + 2 * self.radius > self.screen.get_height():
           self.speed_y = self.speed_y * -1

        if self.speed_y + self.y < 0:
           self.speed_y = self.speed_y * -1


        self.x = self.speed_x + self.x
        self.y = self.speed_y + self.y


















def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()


    # TODO: Create an instance of the Ball class
    new_ball = Ball(screen, 4, 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))
        new_ball.move()
        new_ball.draw()
        # TODO: Move the ball

# TODO: Draw the ball



        pygame.display.update()


main()
