import pygame, sys, random, time
from pygame.locals import *

class Player:
    def __init__(self, screen, column, direction, color):
        self.screen = screen
        self.x = 125
        self.y = 760
        self.column = column
        self.direction = direction
        self.color = color
        self.lives = 2

    def draw(self):
        #pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x+50, self.y-20), (self.x + 100, self.y), (self.x + 100, self.y +50), (self.x + 50, self.y +30), (self.x, self.y +50)])
        if self.direction:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 66), (self.x + 75, self.y - 100), (self.x + 150, self.y - 66), (self.x + 150, self.y), (self.x + 75, self.y - 33)], 2)
            # pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x+50, self.y-20), (self.x + 100, self.y), (self.x + 100, self.y +50), (self.x + 50, self.y +30), (self.x, self.y +50)])
        else:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 66), (self.x + 75, self.y - 33), (self.x + 150, self.y - 66), (self.x + 150, self.y), (self.x + 75, self.y + 33)], 2)
            #pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x+50, self.y + 20), (self.x + 100, self.y), (self.x + 100, self.y +50), (self.x + 50, self.y + 70), (self.x, self.y +50)])
    def move(self):
        pass
    def isHit(self, enemy):
        return pygame.Rect(self.x, self.y - 33, self.x +150, self.y+100).collidepoint(enemy.x, enemy.y)


class Enemy:
    def __init__(self, screen, column, y, speed):
        self.screen = screen
        self.column = column
        self.direction = random.choice([True, False])
        self.color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
        self.x = 125
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
        self.enemy_list.append(Enemy(self.screen, 1, 0, 5))

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

    def isAtBottom(self):
        for enemy in self.enemy_list:
            if enemy.y > self.screen.get_height():
                self.enemy_list.remove(enemy)
            elif enemy.y > self.screen.get_height() - 33 and not enemy.direction:
                self.enemy_list.remove(enemy)

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
    screen = pygame.display.set_mode((400, 800))

    player = Player(screen, 1, True, (255, 0, 0))
    enemy_list = EnemyList(screen)
    gameclock = time.time()
    score = Score(screen)
    enemy_list.spawn()
    up_hit = pygame.mixer.Sound("sword_hit.wav")
    down_hit = pygame.mixer.Sound("shield_hit.wav")
    lives = 3
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

            # -EXIT-
            if event.type == pygame.QUIT:
                sys.exit()
        if gameclock + 2 < time.time():
            enemy_list.spawn()
            gameclock = time.time()
        for enemy in enemy_list.enemy_list:
            if player.isHit(enemy) and player.direction == enemy.direction and player.color == enemy.color:
                if player.direction:
                    pygame.mixer.Sound.play(up_hit)
                else:
                    pygame.mixer.Sound.play(down_hit)
                enemy.is_hit = True
                score.score += 100
        enemy_list.removeHitEnemies()
        enemy_list.isAtBottom()
        screen.fill(pygame.Color("Black"))
        player.draw()
        enemy_list.draw()
        enemy_list.move()
        score.draw()
        pygame.display.update()

main()