import pygame, sys, random, time
from pygame.locals import *

class Column:
    def __init__(self, screen):
        self.screen = screen

    def getX(self, column):
        return (column * int(self.screen.get_width()/3)) + 25
    def draw(self):
        pygame.draw.line(self.screen, (100, 100, 100), (200, 10), (200, 790), 2)
        pygame.draw.line(self.screen, (100, 100, 100), (400, 10), (400, 790), 2)

class Player:
    def __init__(self, screen, x, column, direction, color):
        self.screen = screen
        self.column = column
        self.x = x
        self.y = 760
        self.canBlock = False
        self.direction = direction
        self.color = color
        self.lives = 3

    def draw(self):
        if self.direction:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 66), (self.x + 75, self.y - 100), (self.x + 150, self.y - 66), (self.x + 150, self.y), (self.x + 75, self.y - 33)], 2)
        else:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 66), (self.x + 75, self.y - 33), (self.x + 150, self.y - 66), (self.x + 150, self.y), (self.x + 75, self.y + 33)], 2)
    def move(self):
        pass
    def isHit(self, enemy):
        return pygame.Rect(self.x, self.y - 33, self.x +150, self.y+100).collidepoint(enemy.x, enemy.y)
    def drawHealth(self):
        if self.lives == 3:
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - 20, 10, 10, 10), 2)
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - 35, 10, 10, 10), 2)
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - 50, 10, 10, 10), 2)
        elif self.lives == 2:
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - 20, 10, 10, 10), 2)
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - 35, 10, 10, 10), 2)
        elif self.lives == 1:
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - 20, 10, 10, 10), 2)
        else:
            pass

    def drawShield(self):
        pygame.draw.polygon(self.screen, self.color,
                            [(self.x - 10, self.y - 76), (self.x + 75, self.y - 130), (self.x + 160, self.y - 76),
                             (self.x + 75, self.y - 120)], 2)
        # if self.direction:
        #     pygame.draw.polygon(self.screen, self.color, [(self.x - 10, self.y - 76), (self.x + 75, self.y - 130), (self.x + 160, self.y - 76), (self.x + 75, self.y - 120)], 2)
        # else:
        #     pygame.draw.polygon(self.screen, self.color, [(self.x - 10, self.y - 76), (self.x + 75, self.y - 44), (self.x + 160, self.y - 76), (self.x + 75, self.y - 54)], 2)



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

    def spawn(self):
        self.enemy_list.append(Enemy(self.screen, random.randint(0, 2), 0, 5))

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
    pygame.display.set_caption("cool gaem")
    screen = pygame.display.set_mode((600, 800))

    player = Player(screen, 1, 0, True, (255, 0, 0))
    enemy_list = EnemyList(screen)
    gameclock = time.time()
    score = Score(screen)
    enemy_list.spawn()
    up_hit = pygame.mixer.Sound("sword_hit.wav")
    down_hit = pygame.mixer.Sound("shield_hit.wav")
    font = pygame.font.Font(None, 50)
    column = Column(screen)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            # -SWITCH PLAYER DIRECTION-
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP] and player.direction == False:
                player.direction = True
            elif pressed_keys[K_DOWN] and player.direction == True:
                player.direction = False

            # -SWITCH PLAYER COLOR-
            if pressed_keys[K_a]:
                player.color = (255, 0, 0)
            elif pressed_keys[K_s]:
                player.color = (0, 255, 0)
            elif pressed_keys[K_d]:
                player.color = (0, 0, 255)
            # -SET PLAYER COLUMN-
            if pressed_keys[K_LEFT] and not player.column == 0:
                player.column -= 1
            elif pressed_keys[K_RIGHT] and not player.column == 2:
                player.column += 1

            # -EXIT-
            if event.type == pygame.QUIT:
                sys.exit()



        if player.lives < 1:
            text_as_image = font.render("Game Over!", False, (255, 255, 255))
            screen.blit(text_as_image, (200, 400))
        else:
            player.x = column.getX(player.column)
            if gameclock + 2 < time.time():
                enemy_list.spawn()
                gameclock = time.time()
            for enemy in enemy_list.enemy_list:
                enemy.x = column.getX(enemy.column)
                if player.isHit(enemy) and player.direction == enemy.direction and player.color == enemy.color:
                    if player.direction:
                        pygame.mixer.Sound.play(up_hit)
                    else:
                        pygame.mixer.Sound.play(down_hit)
                    enemy.is_hit = True
                    score.score += 100
                elif player.isHit(enemy):
                    enemy.is_hit = True
                    player.lives -= 1
            enemy_list.removeHitEnemies()
            enemy_list.isAtBottom(player)
            screen.fill(pygame.Color("Black"))
            player.draw()
            player.drawShield()
            player.drawHealth()
            enemy_list.draw()
            column.draw()
            enemy_list.move()
            score.draw()
        pygame.display.update()


main()