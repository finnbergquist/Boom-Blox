import serial
import time

new = False;

# set up the serial line
ser = serial.Serial('/dev/cu.usbmodem143101', 9600)
time.sleep(2)

# Read input from Arduino
for i in range(50):
    b = ser.readline()         # read a byte string
    n = b.decode()  # decode byte string into Unicode 
    MIDI = n.split(':')[0]
    effect = n.split(':')[1]
    inst = n.split(':')[2]
    print(inst)
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()


#run audio loop
