import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.y = 591
        self.exploded = False

    def move(self):
        self.y -= 5

    def draw(self):
        pygame.draw.line(self.screen, (0, 255, 0) ,(self.x, self.y), (self.x, self.y - 8), 4)


class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.missiles = []
        self.image = pygame.image.load("fighter.png")
        self.image.set_colorkey((255, 255, 255))


    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        new_missile = Missile(self.screen, self.x + 50)
        self.missiles.append(new_missile)

    def remove_exploded_missiles(self):
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.dead = False
        self.originalX = x
        self.move_right = True
        self.image = pygame.image.load("badguy.png")
        self.image.set_colorkey((0,0,0))

    def move(self):
        if self.move_right:
            self.x += 5
            if self.x > self.originalX + 100:
                self.move_right = False
                self.y += 15
        else:
            self.x -= 5
            if self.x < self.originalX - 100:
                self.move_right = True
                self.y += 15

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(missile.x, missile.y)


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20))

    @property
    def is_defeated(self):
        return len(self.badguys) == 0

    def move(self):
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].dead:
                del self.badguys[k]
class Scoreboard:
    def __init__(self, screen, ):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 30)
    def draw(self):
        text_as_image = self.font.render("Score: "+ str(self.score), True, (255, 255, 255))
        self.screen.blit(text_as_image, (5, 5))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    gameover_image = pygame.image.load("gameover.png")
    screen = pygame.display.set_mode((640, 650))
    enemy_rows = 3
    enemy = EnemyFleet(screen, enemy_rows)
    scoreboard = Scoreboard(screen)
    fighter = Fighter(screen, 320, 590)
    missile = Missile(screen, fighter.x)
    gameover = False
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN and pressed_keys[K_SPACE]:
                fighter.fire()

        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and fighter.x > -50:
            fighter.x -= 5
        if pressed_keys[pygame.K_RIGHT] and fighter.x < screen.get_width() - 50:
            fighter.x += 5
        fighter.draw()
        for missile in fighter.missiles:
            missile.move()
            missile.draw()
        for badguy in enemy.badguys:
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    badguy.dead = True
                    missile.exploded = True
                    scoreboard.score += 100

        fighter.remove_exploded_missiles()
        enemy.remove_dead_badguys()
        if enemy.is_defeated:
            enemy_rows += 1
            enemy = EnemyFleet(screen, enemy_rows)
        enemy.move()
        enemy.draw()
        scoreboard.draw()
        if not gameover:
            pygame.display.update()
            for badguy in enemy.badguys:
                if badguy.y > 545:
                    gameover = True
                    screen.blit(gameover_image, (170, 200))
                    pygame.display.update()


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
