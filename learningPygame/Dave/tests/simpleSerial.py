import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14202', 115200, timeout = 1000)

for k in range(100):
    print("test " + str(k) + " ", end='')
    print(ser.read(5))
    time.sleep(1)

print("done")