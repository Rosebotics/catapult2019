import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)
        pass

    def move(self):
        self.y = self.y + self.speed
        pass

    def off_screen(self):
        if self.y > self.screen.get_height():
            return True
        else:
            return False
        pass

    def draw(self):

        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y-5), 2)
        pass


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # TODO 16: Initialize this Hero, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of this Hero to x and y.
        # TODO    - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        # TODO    - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        # TODO    - Set the "last hit time" to 0.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0
        pass

    def draw(self):

        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))
        """ Draws this sprite onto the screen. """
        # TODO 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:
        # TODO 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        # TODO    If the current time is greater than this Hero's last_hit_time + 1,
        # TODO      draw this Hero WITHOUT an umbrella,
        # TODO      otherwise draw this Hero WITH an umbrella.
        pass

    def hit_by(self, raindrop):
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))



class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # TODO 24: Initialize this Cloud, as follows:
        # TODO    - Store the screen.
        # TODO    - Set the initial position of this Cloud to x and y.
        # TODO    - Set the image of this Cloud to the given image filename.
        # TODO    - Create a list for Raindrop objects as an empty list called raindrops.
        # TODO  Use instance variables:
        # TODO     screen  x  y  image   raindrops.
        pass

    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 25: Draw (blit) this Cloud's image at its current position.
        pass

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # TODO 28: Append a new Raindrop to this Cloud's list of 03-Raindrops,
        # TODO    where the new Raindrop starts at:
        # TODO      - x is a random integer between this Cloud's x and this Cloud's x + 300.
        # TODO      - y is this Cloud's y + 100.
        pass


def main():
    """ VARIABLES: """
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 600))
    """ PRE-INIT """
    pygame.display.set_caption("rainman")
    testDrop = Raindrop(screen, 320, 10)
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "mike.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(90)
        screen.fill((255, 255, 255))
        testDrop.draw()
        testDrop.move()
        mike.draw()
        if testDrop.off_screen():
            testDrop.y = 10
        if mike.hit_by(testDrop):
            mike.last_hit_time = time.time()

        pygame.display.update()



    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """




    # TODO 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.

    # TODO 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.


        # TODO 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        # TODO    Arrange so that the Cloud moves:
        # TODO      5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # TODO      5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        # TODO      5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        # TODO      5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.



        # TODO 14: As a temporary test, check if test_drop is off screen, if so reset the y position to 10
        # TODO 10: As a temporary test, draw test_drop

        # TODO 20: As a temporary test, check if test_drop is hitting Mike, if so set Mike's last_hit_time
        # TODO 22: When you run this test, slow the rain down to a speed of 2 to see the result, then remove that code

        # TODO 26: Draw the Cloud.

        # TODO 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # TODO: Inside the game loop, make the Cloud "rain", and then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
            # TODO      - move the Raindrop.
            # TODO      - draw the Raindrop.
            # TODO  30: if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # CONSIDER  - if the Raindrop is off the screen, delete it from the Cloud's list of 03-Raindrops.

        # TODO 18: Draw the Hero

        # TODO 6: Update the display and remove the pass statement below





main()