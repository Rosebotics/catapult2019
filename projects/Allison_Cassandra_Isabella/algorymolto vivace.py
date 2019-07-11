import pygame
import sys

class Dancer:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):

        pass

class Blueright:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(self.screen, (10, 165, 225), (self.x, self.y), 40)

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with the xy point of the given missile.
        # Return False otherwise.
       return pygame.Rect(self.x, self.y, 70, 45).collidepoint((missile.x, missile.y)) #TODO: Fix "missile"

class Pinkleft:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(self.screen, (230, 10, 150), (self.x, self.y), 40)

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with the xy point of the given missile.
        # Return False otherwise.
       return pygame.Rect(self.x, self.y, 70, 45).collidepoint((missile.x, missile.y)) #TODO: Fix "missile"


class Purpledown:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(self.screen, (191, 0, 254), (self.x, self.y), 40)

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with the xy point of the given missile.
        # Return False otherwise.
       return pygame.Rect(self.x, self.y, 70, 45).collidepoint((missile.x, missile.y)) #TODO: Fix "missile"

class Yellowup:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(self.screen, (255, 240, 0), (self.x, self.y), 40)

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with the xy point of the given missile.
        # Return False otherwise.
       return pygame.Rect(self.x, self.y, 70, 45).collidepoint((missile.x, missile.y)) #TODO: Fix "misse"

class HPBar:
    def __init__(self, screen):
        self.screen = screen
        self.score = 1000
        self.font = pygame.font.Font(None, 30)
    def draw(self):
        text_as_image = self.font.render("Health:" + str(self.score), True, (155, 75, 160))
        self.screen.blit(text_as_image, (5, 5))


def main():

    pinkleft = Pinkleft
    purpledown = Purpledown
    yellowup = Yellowup
    blueright = Blueright
    hpbar = HPBar
    dancer = Dancer

    pygame.mixer.music.load("albatraoz.mp3")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        hpbar.draw()
        dancer.draw()
        dancer.move()
        pinkleft.move()
        pinkleft.draw()
        purpledown.move()
        purpledown.draw()
        yellowup.move()
        yellowup.draw()
        blueright.move()
        blueright.draw()

        if pinkleft.hit_by:
            pinkleft.dead = True

        if purpledown.hit_by:
            purpledown.dead = True

        if yellowup.hit_by:
            yellowup.dead = True

        if blueright.hit_by:
            blueright.dead = True

        if dancer.hit_by:
            hpbar.score = hpbar.score - 100





    screen.fill(0, 0, 0)

    scoreboard.draw()