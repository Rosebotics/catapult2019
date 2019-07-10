import pygame, sys, time, math, random


class Ball:
    def __init__(self, screen, x, y, speed, color, radius):
        self.screen = screen
        self.x = int(x)
        self.y = int(y)
        self.Xspeed = speed
        self.Yspeed = speed
        self.color = color
        self.radius = radius

        self.angle = 45

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    def move(self):
        if self.x > self.screen.get_width():
            self.Xspeed *= -1
        if self.x < 0:
            self.Xspeed = abs(self.Xspeed)
        if self.y > self.screen.get_height():
            self.Yspeed *= -1
        if self.y < 0:
            self.Yspeed = abs(self.Yspeed)

        self.x += self.Xspeed
        self.y += self.Yspeed
    def spawn(self, number):
        for i in range(number):
            newBall = Ball(self.screen, random.randint(0, self.screen.get_width()), random.randint(0, self.screen.get_height()), 5, (random.int(0, 255), (random.int(0, 255), (random.int(0, 255)), 15)))

