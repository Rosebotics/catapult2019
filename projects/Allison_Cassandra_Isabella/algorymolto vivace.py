import pygame
import sys

class Dancer:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y

    self.image_umbrella = pygame.image.load(with_umbrella_filename)
    self.image_no_umbrella = pygame.image.load(without_umbrella_filename)

def draw(self):
    # Draw this Fighter, using its image at its current (x, y) position.
    self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        pass

class Orb:
    def __init__(self, screen, x, y, direction):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.xspeed = 0
        self.yspeed = 0
        if direction == 'up':
            self.color = (255, 240, 0)
            self.yspeed = -5    # TODO: set speeds to something
        elif direction == 'down':
            self.color = (191, 0, 254)
            self.yspeed = 5
        elif direction == 'left':
            self.color = (230, 10, 150)
            self.xspeed = -5
        elif direction == 'right':
            self.color = (0, 255, 225)
            self.xspeed = 5

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 30)

    def hit_by(self, missile):      # TODO: make this work
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with the xy point of the given missile.
        # Return False otherwise.
       #return pygame.Rect(self.x, self.y, 70, 45).collidepoint((missile.x, missile.y))
        pass

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

class HPBar:
    def __init__(self, screen):
        self.screen = screen
        self.score = 1000
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        text_as_image = self.font.render("Health:" + str(self.score), True, (155, 75, 160))
        self.screen.blit(text_as_image, (5, 5))


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 640))

    pinkleft = Orb(screen, 50, 50, 'left') # TODO: Change temporary Xs and Ys
    purpledown = Orb(screen, 60, 60, 'down')
    yellowup = Orb(screen, 70, 70, 'up')
    blueright = Orb(screen, 80, 80, 'up')
    hpbar = HPBar(screen)
    dancer = Dancer(screen, 90, 90)
    pygame.mixer.music.load("albatraoz.mp3")

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        hpbar.draw()

        # if pinkleft.hit_by:
        #     pinkleft.dead = True
        # if purpledown.hit_by:
        #     purpledown.dead = True
        # if yellowup.hit_by:
        #     yellowup.dead = True
        # if blueright.hit_by:
        #     blueright.dead = True
        # if dancer.hit_by:
        #     hpbar.score = hpbar.score - 100
        #if hp
        hpbar.draw()
        pygame.display.update()


main()