import pygame, sys, random, time
import serial


def main():
    ser = serial.Serial('/dev/cu.usbmodem14202', 115200, timeout=0)

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Punch Test")
    screen = pygame.display.set_mode((640, 650))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        serial_data = ser.read()
        if serial_data:
            message = serial_data.decode('utf-8')
            print(message, end='')

        screen.fill((0, 0, 0))
        pygame.display.update()

main()
