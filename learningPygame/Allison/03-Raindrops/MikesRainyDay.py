import pygame
import sys
import time  # Note this!
import random  # Note this!
random.seed()

class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # DONE 8: Initialize this Raindrop, as follows:
        # DONE    - Store the screen.
        # DONE    - Set the initial position of the Raindrop to x and y.
        # DONE    - Set the initial speed to a random integer between 5 and 15.
        # DONE  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # DONE 11: Change the  y  position of this Raindrop by its speed.
        self.y += self.speed
        pass

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # DONE 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > 800

    def draw(self):
        """ Draws this sprite onto the screen. """
        # DONE 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # DONE     from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, (0, 0, 150), (self.x, self.y), (self.x, self.y + 5), 2)

class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # DONE 16: Initialize this Hero, as follows:
        # DONE    - Store the screen.
        self.screen = screen
        # DONE    - Set the initial position of this Hero to x and y.
        self.x = x
        self.y = y
        # DONE    - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        self.withBrella = pygame.image.load(with_umbrella_filename)
        # DONE    - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        self.noBrella = pygame.image.load(without_umbrella_filename)
        # DONE    - Set the "last hit time" to 0.
        self.last_hittime = 0
        # DONE  Use instance variables:
        # DONE     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.

    def draw(self):
        """ Draws this sprite onto the screen. """
        # DONE 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:

        # DONE 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        # DONE    If the current time is greater than this Hero's last_hit_time + 1,
        # DONE      draw this Hero WITHOUT an umbrella,
        # DONE      otherwise draw this Hero WITH an umbrella.
        if(time.time()) > self.last_hittime + 1:
            self.screen.blit(self.noBrella, (self.x, self.y))
        else:
            self.screen.blit(self.withBrella, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # DONE 19: Return True if this Hero is currently colliding with the given Raindrop.
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # DONE 24: Initialize this Cloud, as follows:
        # DONE    - Store the screen.
        # DONE    - Set the initial position of this Cloud to x and y.
        # DONE    - Set the image of this Cloud to the given image filename.
        # DONE    - Create a list for Raindrop objects as an empty list called raindrops.
        # DONE  Use instance variables:
        # DONE     screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        # DONE 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # DONE 28: Append a new Raindrop to this Cloud's list of Raindrops,
        # DONE    where the new Raindrop starts at:
        # DONE      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # DONE      - y is this Cloud's y + 100.
        new_drop = Raindrop(self.screen, self.x + random.randint(0, 300), self.y + 100)
        self.raindrops.append(new_drop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Mike's Rainy Day")
    clock = pygame.time.Clock()
    mike = Hero(screen, 300, 400, 'Mike_umbrella.png', 'Mike.png')
    cloud = Cloud(screen, 300, 50, 'cloud.png')
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[pygame.K_UP]:
            cloud.y -= 5
        if pressedkeys[pygame.K_DOWN]:
            cloud.y += 5
        if pressedkeys[pygame.K_LEFT]:
            cloud.x -= 5
        if pressedkeys[pygame.K_RIGHT]:
            cloud.x += 5
        screen.fill((255, 255, 255))
        cloud.draw()
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hittime=time.time()
        mike.draw()
        pygame.display.update()


main()
