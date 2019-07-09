import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    # TODO: Return the actual distance between point 1 and point 2.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )
    distance = math.sqrt((point1_x-point2_x)**2 +(point1_y-point2_y)**2)
    return distance

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)


    frame_color = (0, 0, 0)

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    text_background_color = frame_color

    instructions_image = font.render(instruction_text, True, text_color, text_background_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3



    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
               #print(click_position)
                distance_from_circle = distance(click_position, circle_center)
                print(distance_from_circle)

                pygame.mixer.music.load("drums.wav")
                if distance_from_circle < circle_radius:
                    message_text = 'Bullseye!  :)'
                    pygame.mixer.music.play(-1)
                else:
                    message_text = 'You Missed! :( '
                    pygame.mixer.music.stop()


        screen.fill(frame_color)


        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

        message_image = font.render(message_text, True, (0, 0, 0), (122, 237, 201))

        screen.blit(instructions_image, (25, 25))

        screen.blit(message_image,(140,100))

        pygame.display.update()


main()
