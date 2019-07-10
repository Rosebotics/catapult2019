import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)


    def move(self):
        self.y = self.y + self.speed


    def off_screen(self):
        if self.y > self.screen.get_height():
            return True
        else:
            return False


    def draw(self):

        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y-5), 2)



class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0
        pass

    def draw(self):

        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))



class Cloud:
    def __init__(self, screen, x, y, image_filename):

        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []


    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        newDrop = Raindrop(self.screen, self.x + random.randint(0, 300), self.y + random.randint(0, 100))
        self.raindrops.append(newDrop)


def main():
    """ VARIABLES: """
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 600))
    """ PRE-INIT """
    pygame.display.set_caption("rainman")
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "mike.png")
    cloud = Cloud(screen, 300, 50, "cloud.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(90)
        key = pygame.key.get_pressed()

        screen.fill((255, 255, 255))
        cloud.rain()
        if key[pygame.K_RIGHT]:
            cloud.x += 5
        else:
            if key[pygame.K_LEFT]:
                cloud.x -= 5
        if key[pygame.K_UP]:
            cloud.y -= 5
        else:
            if key[pygame.K_DOWN]:
                cloud.y += 5
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        mike.draw()
        cloud.draw()
        pygame.display.update()
main()