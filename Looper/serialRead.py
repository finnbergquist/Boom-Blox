import serial
import time


# set up the serial line
port = '/dev/cu.usbmodem143101'
ser = serial.Serial(port, 9600, timeout=0.1)
time.sleep(2)

# Read input from Arduino
while True:
    data = ser.readline()         # read a byte string
    n = data.decode()  # decode byte string into Unicode 
    string = n.rstrip() # remove \n and \r
    # if it is a string we care about 
    if (":" in string):
        MIDI = n.split(':')[0]
        effect = n.split(':')[1]
        inst = n.split(':')[2]
        print(MIDI)
    

# ser.close()


#run audio loop
