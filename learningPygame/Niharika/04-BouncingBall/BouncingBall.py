import pygame
import sys
import random


# done: Create a Ball class.
# done: Member variables: screen, color, x, y, radius, speed_x, speed_y
# done: Methods __init__, draw, move

class Ball:
    def __init__(self, screen, x , y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = random.randint(5,15)
        self.speed_y = random.randint(5,15)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 15, 15)

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        if self.x > 275 or self.x < 25:
            self.speed_x = - self.speed_x
        if self.y > 275 or self.y < 25 :
            self.speed_y = - self.speed_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # done: Create an instance of the Ball class

    testball = Ball(screen, 50, 150)
    balls =[]

    for x in range(10):
        ball = Ball(screen, random.randint(25,275), random.randint(25,275))
        balls.append(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if event.type :
            #     test_position = event.pos
            #     print(test_position)

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # done: Move the ball
        # done: Draw the ball

        # testball.draw()
        # testball.move()

        for ball in balls:
            ball.move()
            ball.draw()
        pygame.display.update()


main()
