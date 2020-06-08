"""Audio Looper driver method"""
import time
import serial
# from gpiozero import MCP3008, PWMLED
from looper import Looper
from sound_files import mix


##MIGHT NOT NEED WITH LOOPER METHOD
# # Set the channel and step clip 
# def set_clip(instr, channels, steps, clip):
#     for i in range(channels):
#         for j in range(steps):
#             instr.set_audio_num(i, j, clip)

    
def play_region(instr, channel_number):
    ##play loop from channel number 
    mixer.play(instr.get_loop(channel_number), channel_number)


def start_loop(instr):
    """Executable loop. It updates channel volumes on 0.1 second intervals, and plays
    the next step in the sequence every 2 seconds. Loops after 8 steps"""    
    ##get number of channels
    #num_ch = instr.num_channels
    step = -1
    next_time = time.time()
    # mixer.update_channel_volume(0, pot0.value)#setup the channel volumes before audio playback
    # mixer.update_channel_volume(1, pot1.value)
    while True:#audio loop
        play_region(instr, 0)
        #Sleep for however long the audio is 
        time.sleep(1)
        # if time.time() >= next_time:
        #     play_region(instr, 0)
        #     next_time += 1
           
def sort(input, threshold):
    #sort the serial data into specific channels 
    #if its around 40 its 1, 100 its 2, 180 its 3, it its 0, then be default
    if (abs(input - 0) < threshold):
        return 0
    elif (abs(input - 40) < threshold):
        return 1
    elif (abs(input - 100) < threshold):
        return 2
    elif (abs(input - 183) < threshold):
        return 3
    else:
        return "error: can't identify node"


"""
# set up the serial line
port = '/dev/cu.usbmodem143101'
ser = serial.Serial(port, 9600, timeout=0.1)
time.sleep(2)

# Read input from Arduino
while True:
    #initialize output as 000
    output = "000"
    data = ser.readline()         # read a byte string
    n = data.decode()  # decode byte string into Unicode
    string = n.rstrip() # remove \n and \r
    # if it is a string we care about
    if (":" in string):
        #get the resistor value, make it an int, sort it and then 
        #turn it back into a string
        MIDI = str(sort(int(n.split(':')[0]), 10))
        effect = str(sort(int(n.split(':')[1]), 10))
        inst = str(sort(int(n.split(':')[2]), 10))
        #make 3-digit code
        output = MIDI+effect+inst
        
    print(output)
    
"""

    #RUN AUDIO LOOP
while True:
    #settig up channel data
    TEMPO = 5
    CHANNELS = 1
   
    looper = Looper(TEMPO, CHANNELS)#5 is the tempo, 2 channels, 8 steps
    # sequencer.scan_tracks#not implemented yet
    #output = '001'
    # Set first instrument
    looper.set_loop(CHANNELS, '001')

    #setting up mixer
    mixer = mix()
    #start loop on sequencer
    start_loop(looper)
       

            
    
        
        
        
    

