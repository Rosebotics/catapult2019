import pygame, sys, time, math, random


class Ball:
    def __init__(self, screen, x, y, speed, color, radius):
        self.screen = screen
        self.x = int(x)
        self.y = int(y)
        self.speed = speed
        self.color = color
        self.radius = radius

        self.angle = 45

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    def move(self):
        # Make sure angle is positive, then make sure it's within 360
        # if self.x > self.screen.get_width() or self.y > self.screen.get_height() or self.y < 0:
        #     self.angle = 180 - self.angle
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.angle += 1
            self.x = int(self.screen.get_width()/2)
            self.y = (self.screen.get_height()/2)
        self.angle = abs(self.angle)
        if self.angle > 360:
            self.angle -= 360
        self.x += int(math.sin((self.angle / 360) * math.pi) * self.speed)
        self.y += int(math.cos((self.angle / 360) * math.pi) * self.speed)

