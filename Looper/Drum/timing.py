"""Audio Looper driver method"""
import time
import smbus2
# from gpiozero import MCP3008, PWMLED
from drum_files import mix 
from looper import Looper
import math


# set up the bus
bus = smbus2.SMBus(1)
address = 0x04

def readBus():
    data = bus.read_i2c_block_data(address, 0, 4)
    #if there is an error, return last 
    if (data == [255,255,255,255]):
        return [0,0,0,0]
    else:
        return data

        
def play_region(instr, channel_number):
    ##play loop from channel number 
    mixer.play(instr.get_loop(channel_number), channel_number)

def empty(arr):
    for x in range(len(arr)):
        arr[x] = 0

def start_loop(instr):
    #initial time
    start_time = time.time()
    length = 16
    #set sequences
    metro =      [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    kick =       [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
    closed_hat = [1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0]
    snare =      [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0]
    empty_arr =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    instrument_dict = {0 : kick, 
                       1 : snare,
                       2 : closed_hat,
                       3 : metro } 

    #set loops, THIS IS FUCKING WEIRD 
    instr.set_loop(0, '300')
    instr.set_loop(1, '100')
    instr.set_loop(2, '400')
    instr.set_loop(3, '200')

    #set last time and hit time
    last = -1
    hit_time = 0

    #vartiables  for button and inst
    recording = 0
    play = 0
    #to measure how far from the loop starting we are
    #important for first instr hit and noise checking   
    play_time = time.time()
    inst_state = 0
    last_state = 0

    while True:
               

        #start really keeping track of time 
        raw_time = time.time()       
        elapsed_time = raw_time - start_time
        #*4 is to make floor_time 240 BPM instead of 60, give it 16 beats
        floor_time = math.floor(elapsed_time * 4)
        #roll over if it goes over time
        if (floor_time >= float(length)):
            start_time = time.time()
            elapsed_time = raw_time - start_time
            floor_time = math.floor(elapsed_time)
            hit_time = 0

            #reset array we are recording 
            if (recording == 1):              
                empty(instrument_dict[inst_state]) 
                print(inst_state)
            # for x in range(len(snare)):
            #     print(snare[x])

        #read bus t
        output = readBus()

        # #set vars
        hit = output[0]
        inst_state = output[1] - 1 
        recording = output[2]
        play = output[3]
        #if play is off, stop and its been a lil, if its the first time and its been more
        #than a second or its not the first time and play is pressed, STOP the loop
        if (play == 1 and (raw_time - play_time > .5)):
            print("ehere")
            return time.time()
            break

        # #inst_state
        if (inst_state != last_state and (raw_time - play_time > .5)):
            last_state = inst_state
            play_region(instr, inst_state)

        #if its high, play snare, wait a little before checking again
        if (hit == 1 and (elapsed_time - hit_time) > 0.1):
            play_region(instr,inst_state)  
            hit_time = elapsed_time

            #if we are recording, clear array and add to it 
            if (recording == 1):                   
                if round(hit_time * 4) != length:
                    instrument_dict[inst_state][round(hit_time * 4)] = 1
            


        #when you are at an interval, update which instruments are playing
        if (floor_time != last):
            last = floor_time
        #     for x in instruments:
        #         if(x[last] == 1):
        #             play_region(instr, instruments.index(x))
        #             print(instruments.index(x))
           

            if (kick[last] == 1):
                play_region(looper, 0)
            if (snare[last] == 1):
                 play_region(looper, 2)
            if (closed_hat[last] == 1):
                play_region(looper, 3)

# def record(instr):


        
#wait time for play check
wait_time = time.time()
while True:
    
    elapse = time.time() - wait_time
    #settig up channel data
    TEMPO = 5    #how many instruments
    CHANNELS = 4
    looper = Looper(TEMPO, CHANNELS)#5 is the tempo, 2 channels, 8 steps
    mixer = mix()
    mixer.update_channel_volume(0, 1.0)
    #read bus t
    output = readBus()
    print(output)
    # #set vars
    recording = output[2]
    play = output[3]

    #if play is triggered start loop on sequencer
    if (play == 1 and elapse > 0.1):
        wait_time = start_loop(looper)

       
    

            
    
        
        
        
    

