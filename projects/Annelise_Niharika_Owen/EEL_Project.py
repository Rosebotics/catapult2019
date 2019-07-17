import pygame, sys, random, time

class Player:
    def __init__(self, screen, x, y, ):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('water_bottle.png')

        def moveRight(self):
            self.x = self.x + self.speed

        def moveLeft(self):
            self.x = self.x - self.speed

        def moveUp(self):
            self.y = self.y - self.speed

        def moveDown(self):
            self.y = self.y + self.speed