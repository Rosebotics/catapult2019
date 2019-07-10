import pygame
import sys


# TODO: Create a Ball class.

class Ball:

    def __init__(self, screen, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = 15
        self.speed_y = 15
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

        self.x = self.speed_x + self.x
        self.y = self.speed_y + self.y











def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y))

    # TODO: Create an instance of the Ball class





    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball

# TODO: Draw the ball



        pygame.display.update()


main()
