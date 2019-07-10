import pygame
import sys
import random

# TODO: Create a Ball class.
# TODO: Member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods __init__, draw, move
class Ball:
    def __init__ (self,screen,color,x,y,radius,speed_x,speed_y):

        # variable set up
        self.screen = screen
        self.x = x
        self.y = y
        self.rad =radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.direct_x = 1
        self.direct_y = 1


    def draw(self):
        pygame.draw.circle(self.screen, self.color,(self.x, self.y), self.rad)

    def move(self):
        # setting up the bounsing
        if self.x > self.screen.get_width():
            self.direct_x = -1
        elif self.x < 0:
            self.direct_x = 1
        if self.y > self.screen.get_height():
            self.direct_y = -1
        elif self.y < 0:
            self.direct_y = 1
        #moving the ball to new position
        self.x = self.x + (self.speed_x * self.direct_x)
        self.y = self.y + (self.speed_y * self.direct_y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class
   # setting up to make more then one ball
    balls = []
    for i in range(10):
        # created balls are ni randome in nacher
        #screen, color, x, y, radius, speed x, speed y
        ball = Ball(screen, (random.randint(0,155), random.randint(55,255), random.randint(100,255)), random.randint(50,screen.get_width()-50), random.randint(50,screen.get_height()-50), random.randint(5,15), random.randint(1,10), random.randint(1,10))
        balls.append(ball)

    while True:
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
                #press space to add new balls
            if pressed_keys[pygame.K_SPACE]:
                # can change how many are made at a time
               for i in range(100):
                    ball = Ball(screen, (random.randint(0,155), random.randint(55,255), random.randint(100,255)), random.randint(50,screen.get_width()-50), random.randint(50,screen.get_height()-50), random.randint(5, 15),random.randint(1, 10), random.randint(1, 10))
                    balls.append(ball)
                # clear the caos
            if pressed_keys[pygame.K_DOWN]:
                balls.clear()

        clock.tick(60)
        # this is able to have meny more balls and not fail
        screen.fill(pygame.Color('gray'))

        for ball in balls:
        # TODO: Move the ball
            ball.move()
        # TODO: Draw the ball
            ball.draw()

        pygame.display.update()


main()
