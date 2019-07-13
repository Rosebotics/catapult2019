import pygame, sys, random, time
from pygame.locals import *


class Column:  # Returns  the x value for a column, draws lines on the screen
    def __init__(self, screen):
        self.screen = screen

    def getX(self, column): # Returns x value for given column
        return (column * int(self.screen.get_width()/3)) + 25
    def draw(self): # Draws lines on screen
        pygame.draw.line(self.screen, (100, 100, 100), (200, 10), (200, 790), 2)
        pygame.draw.line(self.screen, (100, 100, 100), (400, 10), (400, 790), 2)


class Player:  # The player. Draws, detects if itself is hit, draws health bar.
    def __init__(self, screen, x, column, direction, color):
        self.screen = screen
        self.column = column
        self.x = x
        self.y = 760
        self.canBlock = False
        self.direction = direction
        self.color = color
        self.lives = 20

    def draw(self): # Draws the player
        if self.direction:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 66), (self.x + 75, self.y - 100), (self.x + 150, self.y - 66), (self.x + 150, self.y), (self.x + 75, self.y - 33)], 2)
        else:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 66), (self.x + 75, self.y - 33), (self.x + 150, self.y - 66), (self.x + 150, self.y), (self.x + 75, self.y + 33)], 2)

    def isHit(self, enemy): # If called, returns if it's touching the specified enemy
        return pygame.Rect(self.x, self.y - 33, self.x +150, self.y-100).collidepoint(enemy.x, enemy.y)

    def drawHealth(self): # Draws the health bar
        for i in range(self.lives):
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - (20 + i*15), 10, 10, 10), 2)


class Shield:  # Generates Player's shield. Draws and detects if it's hit
    def __init__(self):
        self.time_deployed = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.isDeployed = False

    def draw(self, player): # Draws the shield
        if player.direction:
            pygame.draw.polygon(player.screen, player.color, [(player.x - 10, player.y - 76), (player.x + 75, player.y - 130), (player.x + 160, player.y - 76), (player.x + 75, player.y - 120)], 2)
        else:
            pygame.draw.polygon(player.screen, player.color, [(player.x - 10, player.y - 76), (player.x + 75, player.y - 44), (player.x + 160, player.y - 76), (player.x + 75, player.y - 54)], 2)

    def isHit(self, enemy, player): # Detects if it's hit
        return self.isDeployed and pygame.Rect(player.x, player.y - 76, 150, 30).collidepoint(enemy.x, enemy.y)

    def should_be_deployed(self):
        return self.current_time - self.time_deployed > 500 and not self.isDeployed

    def should_be_retracted(self):
        return self.time_deployed + 300 < self.current_time and self.isDeployed


class Enemy:
    def __init__(self, screen, column, y, speed):
        self.screen = screen
        self.column = column
        self.direction = random.choice([True, False])
        self.color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
        self.x = 0
        self.y = y
        self.speed = speed
        self.is_hit = False

    def draw(self):
        if self.direction:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 36), (self.x + 75, self.y - 70), (self.x + 150, self.y - 36), (self.x + 150, self.y), (self.x + 75, self.y - 33)], 2)
        else:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 36), (self.x + 75, self.y - 3), (self.x + 150, self.y - 36), (self.x + 150, self.y), (self.x + 75, self.y + 33)], 2)

    def move(self):
        self.y += self.speed


class EnemyList:
    def __init__(self, screen):
        self.screen = screen
        self.enemy_list = []

    def spawn(self, speed):
        self.enemy_list.append(Enemy(self.screen, random.randint(0, 2), 0, speed))

    def draw(self):
        for enemy in self.enemy_list:
            enemy.draw()

    def move(self):
        for enemy in self.enemy_list:
            enemy.move()

    def removeHitEnemies(self):
        for enemy in self.enemy_list:
            if enemy.is_hit:
                self.enemy_list.remove(enemy)

    def isAtBottom(self, player):
        for enemy in self.enemy_list:
            if enemy.y > self.screen.get_height():
                self.enemy_list.remove(enemy)
                player.lives -= 1
            elif enemy.y > self.screen.get_height() - 33 and not enemy.direction:
                self.enemy_list.remove(enemy)
                player.lives -= 1


class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 24)

    def draw(self):
        text_as_image = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(text_as_image, (5, 5))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("On Point")
    screen = pygame.display.set_mode((600, 800))

    player = Player(screen, 1, 0, True, (255, 0, 0))
    enemy_list = EnemyList(screen)
    gameclock = time.time()
    score = Score(screen)
    up_hit = pygame.mixer.Sound("sword_hit.wav")
    down_hit = pygame.mixer.Sound("shield_hit.wav")
    font = pygame.font.Font(None, 50)
    column = Column(screen)

    shield = Shield()
    while True:
        clock.tick(60)
        shield.current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()

            # -SWITCH PLAYER DIRECTION-
            if pressed_keys[K_UP] and player.direction == False:
                player.direction = True
            elif pressed_keys[K_DOWN] and player.direction == True:
                player.direction = False

            # -SET PLAYER COLUMN-
            if pressed_keys[K_LEFT] and not player.column == 0:
                player.column -= 1
            elif pressed_keys[K_RIGHT] and not player.column == 2:
                player.column += 1

            # -SWITCH PLAYER COLOR-
            if pressed_keys[K_a]:
                player.color = (255, 0, 0)
            elif pressed_keys[K_s]:
                player.color = (0, 255, 0)
            elif pressed_keys[K_d]:
                player.color = (0, 0, 255)

            # -DEPLOYS SHIELD-
            if pressed_keys[K_SPACE] and shield.should_be_deployed():
                shield.isDeployed = True
                shield.time_deployed = pygame.time.get_ticks()

            # -EXIT-
            if event.type == pygame.QUIT:
                sys.exit()

        if player.lives < 1:
            text_as_image = font.render("Game Over!", False, (255, 255, 255))
            screen.blit(text_as_image, (200, 400))
            if pressed_keys[K_SPACE]:
                main()
        else:
            player.x = column.getX(player.column)

            # -RETRACTS SHIELD-
            if shield.should_be_retracted():
                shield.isDeployed = False

            # -SPAWN ENEMIES
            if gameclock + 2 - score.score * .0001 < time.time():
                enemy_list.spawn(3 + score.score * .0001)
                gameclock = time.time()

            for enemy in enemy_list.enemy_list:
                enemy.x = column.getX(enemy.column)
                if player.isHit(enemy):
                    enemy.is_hit = True
                    player.lives -= 1
                if shield.isHit(enemy, player) and player.direction == enemy.direction and player.color == enemy.color:
                    if player.direction:
                        pygame.mixer.Sound.play(up_hit)
                    else:
                        pygame.mixer.Sound.play(down_hit)
                    enemy.is_hit = True
                    score.score += 100

            enemy_list.removeHitEnemies()
            enemy_list.isAtBottom(player)
            screen.fill(pygame.Color("Black"))
            player.draw()
            player.drawHealth()
            enemy_list.draw()
            column.draw()
            if shield.isDeployed:
                shield.draw(player)
            enemy_list.move()
            score.draw()
        pygame.display.update()


main()