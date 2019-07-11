import pygame, sys, random, time
from pygame.locals import *
import serial

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
        # Draw a horizontal, 1-pixel thick, 8 pixels long, red line on the screen,
        # where the line starts at the current position of this Missile.
        pygame.draw.line(self.screen, (0, 255, 0), (self.x, self.y), (self.x, self.y + 8), 4)


class Fighter:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image. and set its colorkey to white.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("fighter.png")
        self.image.set_colorkey(pygame.Color("White"))
        self.missiles = []

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        self.missiles.append(Missile(self.screen, self.x + 50))

    def remove_exploded_missles(self):
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y):
        # Store the data.
        # Set   dead to False
        #    and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        self.screen = screen
        self.x = x
        self.y = y
        self.dead = False
        self.original_x = x
        self.move_right = True
        self.image = pygame.image.load("badguy.png")
        self.image.set_colorkey(pygame.Color("Black"))

    def move(self):
        # Move 2 units in the current direction in the x.
        # Switch direction if this Badguy's position is more than 100 pixels from its original position.
        #    When the Badguy changes directions move the y down 15 pixels
        if self.move_right:
            self.x = self.x + 2
            if self.x > self.original_x + 100:
                self.move_right = False
                self.y = self.y + 15
        else:
            self.x = self.x - 2
            if self.x < self.original_x - 100:
                self.move_right = True
                self.y = self.y + 15

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with a point the given missile's current position.
        # Return False otherwise.
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(missile.x, missile.y)


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        return len(self.badguys) == 0

    def move(self):
        # Make each badguy in this EnemyFleet move.
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        # Make each badguy in this EnemyFleet draw itself.
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].dead:
                del self.badguys[k]


class Scoreboard:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        as_text = "Score: " + str(self.score)
        as_image = self.font.render(as_text, True, (255, 255, 255))
        self.screen.blit(as_image, (self.x, self.y))


def main():

    ser = serial.Serial('/dev/cu.usbmodem14202', 115200, timeout=0)
    serial_buffer = ''

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!!!")
    screen = pygame.display.set_mode((640, 650))

    enemy_rows = 3
    enemy = EnemyFleet(screen, enemy_rows)

    fighter = Fighter(screen, 320, 590)
    scoreboard = Scoreboard(screen, 5, 5)
    game_over = False

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == QUIT:
                sys.exit()
            if pressed_keys[K_SPACE] and event.type == KEYDOWN:
                fighter.fire()

        serial_data = ser.read()
        while serial_data:
            serial_buffer += serial_data.decode('utf-8')
            if '\r\n' in serial_buffer:
                # print(serial_buffer)
                if 'L' in serial_buffer and fighter.x > -50:
                    fighter.x = fighter.x - 25
                    # print("l", end='')
                if 'R' in serial_buffer and fighter.x < 590:
                    fighter.x = fighter.x + 25
                    # print("r", end='')
                if 'F' in serial_buffer and fighter.x < 590:
                    fighter.fire()
                    # print("f")
                serial_buffer = ''
            serial_data = ser.read()

        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and fighter.x > -50:
            fighter.x = fighter.x - 5
        if pressed_keys[pygame.K_RIGHT] and fighter.x < 590:
            fighter.x = fighter.x + 5

        fighter.draw()

        enemy.move()
        enemy.draw()
        scoreboard.draw()

        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        for badguy in enemy.badguys:
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    scoreboard.score = scoreboard.score + 100
                    badguy.dead = True
                    missile.exploded = True

        fighter.remove_exploded_missles()
        enemy.remove_dead_badguys()

        if enemy.is_defeated:
            enemy_rows = enemy_rows + 1
            enemy = EnemyFleet(screen, enemy_rows)

        if not game_over:
            pygame.display.update()

            # New code to check for your death!
            for badguy in enemy.badguys:
                if badguy.y > 545:
                    game_over = True
                    game_over_image = pygame.image.load("gameover.png").convert()
                    screen.blit(game_over_image, (170, 200))
                    pygame.display.update()


main()
