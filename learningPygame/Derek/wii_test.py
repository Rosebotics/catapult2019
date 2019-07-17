import pygame
import math

def main():
    pygame.init()

    frame = pygame.display.set_mode((500, 500))

    clock = pygame.time.Clock()

    try:
        wii_remote = pygame.joystick.Joystick(0)
    except pygame.error:
        wii_remote = None

    if wii_remote is not None:
        wii_remote.init()

    looking_for_wii_events = True

    rect_x = 250
    rect_y = 250
    rect_width = 50
    rect_height = 50

    while looking_for_wii_events:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                looking_for_wii_events = False
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 4:
                    pass
                    # print("Movement value is: " + str(event.value))
                # if event.value < -0.1 and event.axis == 4:
                #     rect_x += 10
                # if event.value > 0.1 and event.axis == 4:
                #     rect_x += -10
                # if event.axis == 5:
                #     print("Movement along axis 5 with value: " + str(event.value))
            #     # if -0.4 < event.value < 0.4 and event.axis == 4: # -- rotate controller facing up from palm up to palm down / hard controller movement up-down and left-right
                #     print("Axis is: " + str(event.axis))
                #     print("Value is: " + str(event.value))
                # if abs(event.value) < 0.0001:
                #     print("Axis is: " + str(event.axis))
                #     print("Value is: " + str(event.value))

        frame.fill((255, 255, 255))

        pygame.draw.rect(frame, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))

        print("The value of axis 5 is currently: " + str(wii_remote.get_axis(5)))

        # for i in range(pygame.joystick.get_count()):
        #     print(pygame.joystick.Joystick(i).get_name())

        # print("Wii remote's name is: " + wii_remote.get_name())
        # print("Wii remote's id is: " + str(wii_remote.get_id()))

        # print("Wii remote up button: " + str(round(wii_remote.get_axis(0)) == -1))
        # print("Wii remote down button: " + str(round(wii_remote.get_axis(0)) == 1))
        # print("Wii remote right button: " + str(round(wii_remote.get_axis(1)) == -1))
        # print("Wii remote left button: " + str(round(wii_remote.get_axis(1)) == 1))
        #
        # if wii_remote.get_button(0):  # Button 1
        #     print("Button 1 pressed")
        # elif wii_remote.get_button(1):  # Button 2
        #     print("Button 2 pressed")
        # elif wii_remote.get_button(2):  # A
        #     print("Button A pressed")
        # elif wii_remote.get_button(3):  # B
        #     print("Button B pressed")
        # elif wii_remote.get_button(4):  # Plus
        #     print("Button + pressed")
        # elif wii_remote.get_button(5):  # Minus
        #     print("Button - pressed")
        # elif wii_remote.get_button(6):  # Home
        #     print("Button Home pressed")

        # print(wii_remote.get_hat(0))

        clock.tick(60)

        pygame.display.update()

main()