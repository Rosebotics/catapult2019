import pygame
import sys

class Dancer:


class Blueright:


class Pinkleft:


class Greendown:


class Yellowup:


class HPBar:
    def __init__(self,screen):
        self.screen = screen
        self.score = 1000
        self.font = pygame.font.Font(None, 30)
    def draw(self):
        text_as_image = self.font.render("Score:" + str(self.score), True, (230, 28, 203))
        self.screen.blit(text_as_image, (5, 5))