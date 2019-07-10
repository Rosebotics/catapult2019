import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # done 8: Initialize this Raindrop, as follows:
        # done    - Store the screen.
        # done    - Set the initial position of the Raindrop to x and y.
        # done    - Set the initial speed to a random integer between 5 and 15.
        # done  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5,15) # rest this reset this reset this reset this to (5,15)
        self.colors = [[255,0,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255]]

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # done 11: Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed


    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # done 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        # Done     from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen,self.colors[random.randint(0,5)],(self.x,self.y),(self.x,self.y + 5),2)



class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # done 16: Initialize this Hero, as follows:
        # done    - Store the screen.
        #     - Set the initial position of this Hero to x and y.
        #     - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        #     - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        #     - Set the "last hit time" to 0.
        #   Use instance variables:
        #      screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.
        self.screen = screen
        self.x = x
        self.y =y
        self.image_umbrella = pygame.image.load("Mike_umbrella.png")
        self.image_no_umbrella = pygame.image.load("Mike.png")
        self.last_hit_time = 0

    def draw(self):
        """ Draws this sprite onto the screen. """
        # done 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:
        # done 21: Instead draw (blit) this Hero, at this Hero's position, as follows:
        # done    If the current time is greater than this Hero's last_hit_time + 1,
        # done      draw this Hero WITHOUT an umbrella,
        # done      otherwise draw this Hero WITH an umbrella.
        self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # done 19: Return True if this Hero is currently colliding with the given Raindrop.
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # done 24: Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        #   Use instance variables:
        #      screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        # done 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # done 28: Append a new Raindrop to this Cloud's list of 03-Raindrops,
        #     where the new Raindrop starts at:
        #       - x is a random integer between this Cloud's x and this Cloud's x + 300.
        #       - y is this Cloud's y + 100.
        for i in range(50):
            new_drop = Raindrop(self.screen,random.randint(self.x, self.x + 300), self.y +95 + random.randint(0,5))
            self.raindrops.append(new_drop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    # done 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.set_caption("mikes rany day")
    screen = pygame.display.set_mode((1000,600))
    # done 2: Make a Clock
    clock = pygame.time.Clock()
    # done 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
 #   test_drop = Raindrop(screen, 320, 10)
    # done 15: Make a Hero, named mike, with appropriate images, starting at position x=300 y=400.
    mike = Hero(screen, 300,400,"Mike_unbrella.png","mike.png")
    # done 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50, "cloud.png")
    # done 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
        # done 4:   Make the pygame.QUIT event stop the game.

        # done 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        # done    Arrange so that the Cloud moves:
        # done      5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        # done      5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        # done      5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        # done      5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y +10
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 10
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 10

        # done 5: Inside the game loop, draw the screen (fill with white)
        screen.fill((255,255,255))

        # done 12: As a temporary test, move test_drop
       # test_drop.move()
        # done 14: As a temporary test, check if test_drop is off screen, if so reset the y position to 10
        #if test_drop.off_screen():
        #    test_drop.y = 10
        # done 10: As a temporary test, draw test_drop
        #test_drop.draw()

        # done 20: As a temporary test, check if test_drop is hitting Mike, if so set Mike's last_hit_time
       # if mike.hit_by(test_drop):
          #  mike.last_hit_time = time.time()
        # done 22: When you run this test, slow the rain down to a speed of 2 to see the result, then remove that code

        # done 26: Draw the Cloud.
        cloud.draw()

        # done 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # : Inside the game loop, make the Cloud "rain", and then:
        #     For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # done  30: if the Hero is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # CONSIDER  - if the Raindrop is off the screen, delete it from the Cloud's list of 03-Raindrops.
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
            if raindrop.y > 700 :
                cloud.raindrops.remove(raindrop)

        # done 18: Draw the Hero
        mike.draw()

        # done 6: Update the display and remove the pass statement below
        pygame.display.update()



# TODO: Call main.
main()