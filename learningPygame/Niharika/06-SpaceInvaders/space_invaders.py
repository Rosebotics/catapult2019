import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x):
        # Store the data.  Initialize:   y to 591   and   exploded to False.
        self.screen = screen
        self.x = x
        self.y = 591
        self.exploded = False



    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        self.y = self.y - 5

    def draw(self):
        # Draw a vertical, 4 pixels thick, 8 pixels long, red (or green) line on the screen,
        # where the line starts at the current position of this Missile.
        pygame.draw.line(self.screen, (0, 255, 0), (self.x, self.y), (self.x, self.y - 8), 4)

class Fighter:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image
        # Set the colorkey to white (it has a white background that needs removed)
        self.screen = screen
        self.x = x
        self.y = y
        self.missiles = []
        self.image = pygame.image.load("fighter.png")
        self.image.set_colorkey(pygame.Color("White"))



    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        new_missile = Missile(self.screen, self.x + 50)
        self.missiles.append(new_missile)

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   dead to False   and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        self.screen = screen
        self.x = x
        self.y = y
        self.dead = False


    def move(self):
        # Move 2 units in the current direction.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        pass

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        pass

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with the xy point of the given missile.
        # Return False otherwise.
        pass


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        pass

    def move(self):
        # Make each badguy in this EnemyFleet move.
        pass

    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.
        pass

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].dead:
                del self.badguys[k]

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    # done 9: Set    enemy_rows    to an initial value of 3.
    enemy_rows = 3

    # done 10: Create an EnemyFleet object (called enemy) with the screen and enemy_rows
    enemy = EnemyFleet(screen,enemy_rows)

    # done 1: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen, 320, 590)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # done 5: If the event type is KEYDOWN and pressed_keys[K_SPACE] is True, then fire a missile
            if event.type == QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and pressed_keys[K_SPACE]:
                fighter.fire()


        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # done 3: If K_LEFT is pressed and fighter.x is greater than -50 move the fighter left 5
        if pressed_keys[K_LEFT] and fighter.x > -50:
            fighter.x = fighter.x - 5

        # done 4: If K_RIGHT is pressed and fighter.x is less than 590 move the fighter right 5
        if pressed_keys[K_RIGHT] and fighter.x < 590:
                fighter.x = fighter.x + 5

        # done 2: Draw the fighter
        fighter.draw()

        # TODO 11: Move the enemy
        enemy.move()
        enemy.draw()
        # TODO 12: Draw the enemy

        # done 6: For each missile in the fighter missiles
        for missile in fighter.missiles:
            missile.move()
            missile.draw()
        #   done 7: Move the missile
        #   done 8: Draw the missile

        # TODO 12: For each badguy in the enemy badguys
        #     TODO 13: For each missile in the fighter missiles
        #         TODO 14: If the badguy is hit by the missile
        #             TODO 15: Mark the badguy as dead = True
        #             TODO 16: Mark the missile as exploded = True

        # TODO 17: Use the fighter to remove exploded missiles
        # TODO 18: Use the enemy to remove dead badguys

        # TODO 19: If the enemy is_defeated
        #     TODO 20: Increment the enemy_rows
        #     TODO 21: Create a new enemy with the screen and enemy_rows

        pygame.display.update()


main()


# TODO: After the core game is complete we will implement these tasks:
# Create a Scoreboard class (from scratch)
#   Instance variables: screen, x, y, score, and font (size 30)
#   Methods: draw (and __init__)
# Create a scoreboard at location 5, 5
# Draw the scoreboard in the game loop
# When a Badguy is killed add 100 points to the scoreboard.score
# Check if a Badguy gets a y value greater than 545
#   If that happens show the gameover.png image at (170, 200)
#   Update the display one final time with that image then never again.
