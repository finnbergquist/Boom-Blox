"""Audio Loop driver method"""
import time
# from gpiozero import MCP3008, PWMLED
from channel_structure import channels
from sound_files import mix
import serial
import time

def sort(input, threshold):
    #sort the serial data into specific channels 
    #if its around 40 its 1, 100 its 2, 180 its 3
    if (abs(input - 40) < 10):
        return 1
    elif (abs(input - 100) < 10):
        return 2
    elif (abs(input - 183) < 10):
        return 3
    else:
        return "error: can't identify node"

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


#RUN AUDIO LOOP

#setting up volume knobs
# pot0 = MCP3008(0)#channel 0 of the MPC3008 pins
# pot1 = MCP3008(1)#MCP3008 channel 1

#settig up channel data
# sequencer = channels(5,2,8)#5 is the tempo, 2 channels, 8 steps
# sequencer.scan_tracks#not implemented yet
# print(sequencer.audio_file_struct[0])
# print(sequencer.audio_file_struct[1])

# #setting up mixer 
# mixer = mix()



# def play_region(region_number):
#     """helper method for audio loop"""
#     mixer.play(sequencer.get_audio_num(0, region_number), 0)
#     mixer.play(sequencer.get_audio_num(1, region_number), 1)
#     print(sequencer.get_audio_num(0, region_number))
#     print(sequencer.get_audio_num(1, region_number))


# def start_loop():
#     """Executable loop. It updates channel volumes on 0.1 second intervals, and plays
#     the next step in the sequence every 2 seconds. Loops after 8 steps"""    
#     step = -1
#     next_time = time.time()
#     # mixer.update_channel_volume(0, pot0.value)#setup the channel volumes before audio playback
#     # mixer.update_channel_volume(1, pot1.value)
#     while True:#audio loop
#         if time.time() >= next_time:
#             step = (step + 1) % 160
#             if (step/20).is_integer():#very fast way to test(i think)
#                 play_region(int(step/20))#plays audio files at steps 0,1,2,3,4,5,6,7
#             # mixer.update_channel_volume(0, pot0.value)
#             # mixer.update_channel_volume(1, pot1.value)
#             next_time += 0.1
           
        
# start_loop()
       

            
    
        
        
        
    

