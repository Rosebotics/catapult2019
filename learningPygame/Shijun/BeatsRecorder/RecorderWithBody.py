import pygame
import time
import sys

class Dancer:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = 204
        self.y = 170

        self.image_idle = pygame.image.load('dancer_idle.png')
        self.image_idle = pygame.transform.scale(self.image_idle, (233, 300))
        self.image_leftpunch = pygame.image.load('dancer_leftpunch.png')
        self.image_leftpunch = pygame.transform.scale(self.image_leftpunch, (233, 300))
        self.image_rightpunch = pygame.image.load('dancer_rightpunch.png')
        self.image_rightpunch = pygame.transform.scale(self.image_rightpunch, (233, 300))
        self.image_uppunch = pygame.image.load('dancer_uppunch.png')
        self.image_uppunch = pygame.transform.scale(self.image_uppunch, (233, 300))
        self.image_downpunch = pygame.image.load('dancer_downpunch.png')
        self.image_downpunch = pygame.transform.scale(self.image_downpunch, (233, 300))
        self.image_idle.set_colorkey((0, 0, 0))
        self.image_leftpunch.set_colorkey((0, 0, 0))
        self.image_rightpunch.set_colorkey((0, 0, 0))
        self.image_uppunch.set_colorkey((0, 0, 0))
        self.image_downpunch.set_colorkey((0, 0, 0))

    def draw(self):
        self.screen.blit(self.image_idle, (self.x, self.y))

    def punch_left(self):
        self.screen.blit(self.image_leftpunch, (self.x, self.y))

    def punch_right(self):
        self.screen.blit(self.image_rightpunch, (self.x, self.y))

    def punch_up(self):
        self.screen.blit(self.image_uppunch, (self.x, self.y))

    def punch_down(self):
        self.screen.blit(self.image_downpunch, (self.x, self.y+100))

class Orb:
    def __init__(self, screen, direction):
        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height
        self.color = (0, 0, 0)
        self.xspeed = 0
        self.yspeed = 0
        self.x = 0
        self.y = 0
        self.direction = direction
        self.isdead = False
        if self.direction == 'up':
            self.x = self.screen_width // 2
            self.y = self.screen_height + 30
            self.color = (255, 240, 0)
            self.yspeed = -2
        elif self.direction == 'down':
            self.x = self.screen_width // 2
            self.y = -30
            self.color = (191, 0, 254)
            self.yspeed = 2
        elif self.direction == 'left':
            self.x = -30
            self.y = self.screen_height // 2
            self.color = (230, 10, 150)
            self.xspeed = 2
        elif self.direction == 'right':
            self.x = self.screen_width + 30
            self.y = self.screen_height // 2
            self.color = (0, 255, 225)
            self.xspeed = -2

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 30)

    def hit_by(self, punchDirection):
        return pygame.Rect(94, 60, 453, 520).collidepoint((self.x, self.y)) and punchDirection == self.direction

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

class HPBar:
    def __init__(self, screen):
        self.screen = screen
        self.score = 1000
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        text_as_image = self.font.render("Health:" + str(self.score), True, (155, 75, 160))
        self.screen.blit(text_as_image, (5, 5))


class Face:
    def __init__(self, screen, name):
        self.screen = screen
        if name == "Jared":
            self.image = pygame.image.load("Jared.png")
        self.position = "i"

    def draw(self):
        x = 0
        y = 0
        image = pygame.transform.scale(self.image, (100, 100))
        if self.position == "i":
            x = 240
            y = 130
        elif self.position == "u":
            x = 240
            y = 190
            image = pygame.transform.scale(self.image, (80, 80))
        elif self.position == "d":
            x = 235
            y = 300
            image = pygame.transform.scale(self.image, (80, 80))
        elif self.position == "r":
            x = 230
            y = 130
        elif self.position == "l":
            x = 310
            y = 130
        self.screen.blit(image, (x, y))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Beat Fighter")
    screen = pygame.display.set_mode((640, 640))
    hpbar = HPBar(screen)
    face = Face(screen, "Jared")
    dancer = Dancer(screen, 90, 90)
    funished = pygame.image.load("Funished.png")
    #pygame.mixer.music.load("albatraoz.mp3")
    pygame.mixer.music.load("Chicken Dance.mp3")
    punchbox = (129, 95, 383, 450)
    hurtbox = (204, 170, 233, 300)
    orblist = []

    timeline_dict = {}
    f = open('old_town_road.txt', 'w')

    is_game_over = False

    def game_intro():

        intro = True

        while intro():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(255,255,255)
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("Beat Fighter", largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(15)

    pygame.mixer.music.play()
    start_milli_time = int(round(time.time() * 1000))
    while True:

        clock.tick(250)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 15), punchbox)
        pygame.draw.rect(screen, (0, 0, 0), hurtbox)

        current_milli_time = int(round(time.time() * 1000))
        time_since_start = current_milli_time - start_milli_time
        rounded_time = time_since_start - time_since_start % 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
            elif event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_DOWN]:
                    dancer.punch_down()
                    face.position = "d"
                    line = str(rounded_time) + ",down\n"
                    f.write(line)
                    print(line)
                elif pressed_keys[pygame.K_UP]:
                    dancer.punch_up()
                    face.position = "u"
                    line = str(rounded_time) + ",up\n"
                    f.write(line)
                    print(line)
                elif pressed_keys[pygame.K_LEFT]:
                    dancer.punch_left()
                    face.position = "l"
                    line = str(rounded_time) + ",left\n"
                    f.write(line)
                    print(line)
                elif pressed_keys[pygame.K_RIGHT]:
                    dancer.punch_right()
                    face.position = "r"
                    line = str(rounded_time) + ",right\n"
                    f.write(line)
                    print(line)
        dancer.draw()
        face.position = "i"
        face.draw()
        pygame.display.update()


while True:
    main()
