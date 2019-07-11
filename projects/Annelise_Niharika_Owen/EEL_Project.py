import pygame, sys, random, time

class WaterBottle:

class Head:
    def __init__(self, screen, x, y,):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self.screen, (255, 165, 0), (self.x, self.y), 5)

class Fish:

class Body:

class Scoreboard:

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("EEL!")
    screen = pygame.display.set_mode((650, 650))

    clock.tick(60)
main()