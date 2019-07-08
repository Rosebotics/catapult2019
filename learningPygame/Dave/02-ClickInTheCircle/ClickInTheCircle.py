import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    # TODO: Return the actual distance between point 1 and point 2.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )
    return 0


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

    pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit()

            # TODO 2: For a MOUSEBUTTONDOWN event get the click position.
            # TODO 3: Determine if the distance to the circle_center is less than the circle_radius
            # TODO 4: Set the message_text to either 'Bullseye!' or 'You missed!'
            # TODO 7: After you get the message_text working add the drums.wav
            # TODO 7:   Start playing for clicks within the circle, stop playing for clicks outside the circle

        screen.fill(frame_color)

        # TODO 1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width

        # TODO 5: Create a text image (render the text) based on the message_text
        # TODO 5:   Color (122, 237, 201)
        # TODO 5:   Background Color (122, 237, 201)

        screen.blit(instructions_image, (25, 25))
        # TODO 6: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'

        pygame.display.update()


main()
