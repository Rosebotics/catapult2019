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

    def hurt(self):
        pass

class Orb:
    def __init__(self, screen, direction):
        self.isdead = False
        self.screen = screen
        self.x = 0
        self.y = 0
        self.color = (0, 0, 0)
        self.xspeed = 0
        self.yspeed = 0
        self.direction = direction
        if direction == 'up':
            self.x = 320
            self.y = -30
            self.color = (255, 240, 0)
            self.yspeed = 5    # TODO: set speeds to something
        elif direction == 'down':
            self.x = 320
            self.y = 670
            self.color = (191, 0, 254)
            self.yspeed = -5
        elif direction == 'left':
            self.x = -30
            self.y = 260
            self.color = (230, 10, 150)
            self.xspeed = 5
        elif direction == 'right':
            self.x = 670
            self.y = 260
            self.color = (0, 255, 225)
            self.xspeed = -5

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


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 640))
    hpbar = HPBar(screen)
    dancer = Dancer(screen, 90, 90)
    pygame.mixer.music.load("albatraoz.mp3")
    punchbox = (94, 60, 453, 520)
    hurtbox = (204, 170, 233, 300)
    orblist = []
    while True:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            orblist.append(Orb(screen, 'up'))
        if pressed_keys[pygame.K_w]:
            orblist.append(Orb(screen, 'down'))
        if pressed_keys[pygame.K_w]:
            orblist.append(Orb(screen, 'left'))
        if pressed_keys[pygame.K_w]:
            orblist.append(Orb(screen, 'right'))

        clock.tick(60)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 5), punchbox)
        pygame.draw.rect(screen, (0, 0, 0), hurtbox)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        hpbar.draw()

        #TODO when start clicked
        #TODO: activate hurtbox
        punchway = ''
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN]:
            dancer.punch_down()
            punchway = 'down'
        elif pressed_keys[pygame.K_UP]:
            dancer.punch_up()
            punchway = 'up'
        elif pressed_keys[pygame.K_LEFT]:
            dancer.punch_left()
            punchway = 'left'
        elif pressed_keys[pygame.K_RIGHT]:
            dancer.punch_right()
            punchway = 'right'
        else:
            dancer.draw()

        for orb in orblist:
            orb.move()
            orb.draw()
            if orb.hit_by(punchway):
                orb.isdead = True
        pygame.display.update()
        for orb in orblist:
            if orb.isdead:
                orblist.remove(orb)


main()