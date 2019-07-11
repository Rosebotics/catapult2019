import pygame
import sys
import serial
ser = serial.Serial('/dev/cu.usbmodem14202', 115200, timeout = 1000)
serial_buffer = ''

pygame.init()
pygame.display.set_mode((320,200))
pygame.display.set_caption('Serial communication')
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    serial_data = ser.read()
    while serial_data:
        serial_buffer += serial_data.decode('utf-8')
        if '\r\n' in serial_buffer:
            print(serial_buffer)
            serial_buffer = ''
        serial_data = ser.read()

    for e in [pygame.event.wait()] + pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()