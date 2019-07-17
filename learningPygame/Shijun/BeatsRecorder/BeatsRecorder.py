import pygame
import time

def main():

    # initialize the pygame module
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    f = open('old_town_road.txt', 'w')
    OFFSET = 5
    clock = pygame.time.Clock()
    pygame.mixer.music.load('FRIENDS.mp3')

    pygame.mixer.music.play()
    starting_time = int(round(time.time() * 1000))
    while True:
        clock.tick(250)
        current_time = int(round(time.time() * 1000))
        time_since_start = current_time - starting_time
        rounded_time = time_since_start - (time_since_start % 5) - OFFSET
        print(rounded_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    line = str(rounded_time) + ",up\n"
                    f.write(line)
                    print(line)
                elif pressed_keys[pygame.K_DOWN]:
                    line = str(rounded_time) + ",down\n"
                    f.write(line)
                    print(line)
                elif pressed_keys[pygame.K_LEFT]:
                    line = str(rounded_time) + ",left\n"
                    f.write(line)
                    print(line)
                elif pressed_keys[pygame.K_RIGHT]:
                    line = str(rounded_time) + ",right\n"
                    f.write(line)
                    print(line)

        # Clear the screen and set the screen background
        screen.fill((0, 0, 0))

        pygame.display.update()

    f.close()


main()


