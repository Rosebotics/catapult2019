import pygame, sys, random, time
from pygame.locals import *
import pygame_textinput

# Team 12

res_y = 1000


class Column:  # Returns  the x value for a column, draws lines on the screen
    def __init__(self, screen):
        self.screen = screen

    def getX(self, column): # Returns x value for given column
        return (column * int(self.screen.get_width()/3)) + 25

    def draw(self): # Draws lines on screen
        pygame.draw.line(self.screen, (100, 100, 100), (self.getX(1) - 25, 10), (self.getX(1) - 25, res_y - 10), 2)
        pygame.draw.line(self.screen, (100, 100, 100), (self.getX(2) - 25, 10), (self.getX(2) - 25, res_y - 10), 2)


class Player:  # The player. Draws, detects if itself is hit, draws health bar.
    def __init__(self, screen, x, column, direction, color):
        self.screen = screen
        self.column = column
        self.x = x
        self.y = res_y - 40
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
        return pygame.Rect(self.x, self.y - 33, self.x + 150, self.y- 100).collidepoint(enemy.x, enemy.y)

    def drawHealth(self): # Draws the health bar
        for i in range(self.lives):
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - (25 + i*30), 10, 20, 20), 2)


class Shield:  # Generates Player's shield. Draws and detects if it's hit
    def __init__(self):
        self.time_deployed = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.isDeployed = False

    def draw(self, player):  # Draws the shield
        if player.direction:
            pygame.draw.polygon(player.screen, player.color, [(player.x - 10, player.y - 76), (player.x + 75, player.y - 130), (player.x + 160, player.y - 76), (player.x + 75, player.y - 120)], 2)
        else:
            pygame.draw.polygon(player.screen, player.color, [(player.x - 10, player.y - 76), (player.x + 75, player.y - 44), (player.x + 160, player.y - 76), (player.x + 75, player.y - 54)], 2)

    def isHit(self, enemy, player):  # Detects if it's hit
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
        self.change_direction = False
        self.change_column = False
        self.speeder = False
        self.done_cd = False
        self.done_cc = False
        self.done_s = False
    def draw(self):
        if self.direction:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 36), (self.x + 75, self.y - 70), (self.x + 150, self.y - 36), (self.x + 150, self.y), (self.x + 75, self.y - 33)], 2)
        else:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y), (self.x, self.y - 36), (self.x + 75, self.y - 3), (self.x + 150, self.y - 36), (self.x + 150, self.y), (self.x + 75, self.y + 33)], 2)

    def move(self):
        self.y += self.speed
        if self.speeder and self.y > res_y/3.5 and not self.done_s:
            self.speed += 1
            self.done_s = True
        if self.change_direction and self.y > res_y/3.5 and not self.done_cd:
            self.direction = not self.direction
            self.done_cd = True
        if self.change_column and self.y > res_y/3.5 and not self.done_cc:
            self.column = random.choice([0, 1, 2])
            self.done_cc = True


class EnemyList:
    def __init__(self, screen):
        self.screen = screen
        self.enemy_list = []

    def spawn(self, speed, s, cd, cc, expert):
        enemy = Enemy(self.screen, random.randint(0, 2), 0, speed)
        if expert:
            enemy.change_column = cc
            enemy.change_direction = cd
            enemy.speeder = s

        self.enemy_list.append(enemy)

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

    def isAtBottom(self, player, sound):
        for enemy in self.enemy_list:
            if enemy.y > self.screen.get_height():
                self.enemy_list.remove(enemy)
                player.lives -= 1
                pygame.mixer.Sound.play(sound)
            elif enemy.y > self.screen.get_height() - 33 and not enemy.direction:
                self.enemy_list.remove(enemy)
                player.lives -= 1
                pygame.mixer.Sound.play(sound)


class PlayerInfo:
    def __init__(self, score, playername, id):
        self.playername = playername
        self.score = score
        self.id = id

    def __repr__(self):
        return "%s, %d, %d" % (self.playername,self.score, self.id)

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 24)

    def draw(self):
        text_as_image = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(text_as_image, (5, 5))

class Scoreboard:
    def __init__(self, screen, playername):
        self.screen = screen
        self.playername = playername
        self.list = []


    def record(self, score, playername, id):
        file = open("scores.txt", "a")
        file.write("\n" + str(score) + "," + playername + "," + str(int(id)))
        file.close()

    def read(self):
        file = open("scores.txt", "r")

        content = file.readlines()
        for line in content:
            stripLine = line.strip()
            cleanList = stripLine.split(",")
            score = int(cleanList[0])
            playername = cleanList[1]
            id = int(cleanList[2])
            playerinfo = PlayerInfo(score, playername, id)
            self.list.append(playerinfo)

        self.list = sorted(self.list, key=lambda player_info: (player_info.score, -player_info.id), reverse=True)
        print(self.list)
        file.close()

    def draw(self):
        pass
def get_playername(screen):
    textinput = pygame_textinput.TextInput()
    textinput.text_color = (255, 255, 255)
    textinput.font_object = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()

    active = True
    while active:
        events = pygame.event.get()
        for event in events:
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                exit()
            if pressed_keys[K_RETURN]:
                active = False

        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.get_surface(), (120, 30))
        pygame.display.update()
        clock.tick(30)
    return textinput.get_text()


    active = True
    while active:
        events = pygame.event.get()
        for event in events:
            pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                exit()
            if pressed_keys[K_RETURN]:
                active = False

        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.get_surface(), (120, 30))
        pygame.display.update()
        clock.tick(30)
    return textinput.get_text()

def main():
    playername = ""

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("On Point")
    screen = pygame.display.set_mode((600, res_y))

    player = Player(screen, 1, 1, True, (255, 0, 0))
    scoreboard = Scoreboard(screen, playername)
    enemy_list = EnemyList(screen)
    gameclock = time.time()
    score = Score(screen)
    up_hit = pygame.mixer.Sound("sword_hit.wav")
    down_hit = pygame.mixer.Sound("shield_hit.wav")
    player_hit = pygame.mixer.Sound("player_hit.wav")
    font = pygame.font.Font(None, 50)
    column = Column(screen)
    shield = Shield()
    expert = False
    while True:
        clock.tick(60)
        shield.current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_e] and pressed_keys[K_x] and pressed_keys[K_p] and not expert:
                expert = True
                player.lives = 5
                score.score = 0
                enemy_list.enemy_list = []
            # -SWITCH PLAYER DIRECTION-
            if pressed_keys[K_UP] and not player.direction:
                player.direction = True
            elif pressed_keys[K_DOWN] and player.direction:
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

            if not player.lives == -42:
                screen.fill(pygame.Color("Black"))
                text_score = font.render("Name:", True, (255, 255, 255))
                screen.blit(text_score, (10, 30))
                playername = get_playername(screen)
                screen.fill(pygame.Color("Black"))
                # if expert:
                #     score.score *= 3.5
                #     score.score = int(score.score)
                scoreboard.record(score.score, playername, time.time())
                scoreboard.read()
                print(scoreboard.list)
                length = len(scoreboard.list)
                if length > 10:
                    length = 10
                for e in range(length):
                    print(e)
                    text = font.render(str(e+1) + "    " + str(scoreboard.list[e].playername) + " - " + str(scoreboard.list[e].score), True, (255, 255, 255))
                    screen.blit(text, (10, 100+ 60*e))
                text_score = font.render("High Scores:", True, (255, 255, 255))
                screen.blit(text_score, (10, 30))
            player.lives = -42

        else:
            player.x = column.getX(player.column)

            # -RETRACTS SHIELD-
            if shield.should_be_retracted():
                shield.isDeployed = False
            if expert:
                # -SPAWN EXPERT ENEMIES-
                if gameclock + 2 - score.score * .00008 < time.time():
                    print("Expert Enemy Spawned")
                    enemy_list.spawn(4 + score.score * .0001, random.choice([True, False]), random.choice([True, False]), random.choice([True, False]), expert)
                    gameclock = time.time()

            else:
                # -SPAWN ENEMIES-
                if gameclock + 2 - score.score * .00008 < time.time():
                    print("Enemy Spawned")
                    enemy_list.spawn(4 + score.score * .0001, False, False, False, expert)
                    gameclock = time.time()


            for enemy in enemy_list.enemy_list:
                enemy.x = column.getX(enemy.column)
                if player.isHit(enemy):
                    enemy.is_hit = True
                    player.lives -= 1
                    score.score -= int(score.score * .1)
                    pygame.mixer.Sound.play(player_hit)

                if shield.isHit(enemy, player) and player.direction == enemy.direction and player.color == enemy.color:
                    if player.direction:
                        pygame.mixer.Sound.play(up_hit)
                    else:
                        pygame.mixer.Sound.play(down_hit)
                    enemy.is_hit = True
                    if expert:
                        score.score += 300
                        score.score += int(score.score * (random.randint(2, 4) / 100))
                    else:
                        score.score += 100
                        score.score += int(score.score * (random.randint(1, 2) / 100))


            enemy_list.removeHitEnemies()
            enemy_list.isAtBottom(player, player_hit)
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
