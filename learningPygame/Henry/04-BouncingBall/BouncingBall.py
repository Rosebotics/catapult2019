import pygame, sys, time, math, random
from Ball import Ball

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball = Ball(screen, 150, 150, 5, (0, 0, 0), 15)
    # TODO: Create an instance of the Ball class

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))
        ball.move()
        ball.draw()
        # TODO: Move the ball
        # TODO: Draw the ball

        pygame.display.update()


main()
