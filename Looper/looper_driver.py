"""Audio Looper driver method"""
import time
# from gpiozero import MCP3008, PWMLED
from channel_structure import channels
from sound_files import mix
import serial
import time


# Set the channel and step clip 
def set_clip(instr, channels, steps, clip):
    for i in range(channels):
        for j in range(steps):
            instr.set_audio_num(i, j, clip)

    
def play_region(instr, region_number):
    """helper method for audio loop"""
    mixer.play(instr.get_audio_num(0, region_number), 0)
    mixer.play(instr.get_audio_num(1, region_number), 1)
    # print(sequencer.get_audio_num(0, region_number))
    # print(sequencer.get_audio_num(1, region_number))


def start_loop(instr):
    """Executable loop. It updates channel volumes on 0.1 second intervals, and plays
    the next step in the sequence every 2 seconds. Loops after 8 steps"""    
    step = -1
    next_time = time.time()
    # mixer.update_channel_volume(0, pot0.value)#setup the channel volumes before audio playback
    # mixer.update_channel_volume(1, pot1.value)
    while True:#audio loop
        if time.time() >= next_time:
            step = (step + 1) % 160
            if (step/20).is_integer():#very fast way to test(i think)
                play_region(instr, int(step/20))#plays audio files at steps 0,1,2,3,4,5,6,7
            # mixer.update_channel_volume(0, pot0.value)
            # mixer.update_channel_volume(1, pot1.value)
            next_time += 0.1
           
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
    
# Accessing sounds: 
#     each combination will have a 3-digit code. That code comes from
#     the MIDI, effect and inst inputs. Each of those resistor values
#     will be sorted into a single digit value from 0-10 with the sort 
#     function. Then they will be concatanated into a 3-digit code. 
#     000 representing the default. There will be a dictionary with 
#     these codes that will inform the Raspi which .wav to play.


    #RUN AUDIO LOOP

    #settig up channel data
    tempo = 5
    ch_len= 2
    steps = 8
    sequencer = channels(tempo,ch_len,steps)#5 is the tempo, 2 channels, 8 steps
    # sequencer.scan_tracks#not implemented yet

    # Set first instrument
    set_clip(sequencer, ch_len, steps, output) 
    print(sequencer.audio_file_struct[0])
    print(sequencer.audio_file_struct[1])

    #setting up mixer 
    mixer = mix()
    #start loop on sequencer
    start_loop(sequencer)
       

            
    
        
        
        
    

