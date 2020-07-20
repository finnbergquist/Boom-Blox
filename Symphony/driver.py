from symphony_sound_files import mix
from step_sequencer import step_sequencer
from channel_structure import to_sound_code
import RPi.GPIO as GPIO
import smbus2
import time
import os
import signal
import sys

#setting up buttons
GPIO.setmode(GPIO.BCM)#normal gpio sumbering system
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#setting up i2c bus, bus object passed down to channel_structure to be used for scanning trakcs
#in the other arduino slave
bus = smbus2.SMBus(1)
arduino_address1 = 0x03


#setting up mixer
mixer = mix()
stepSequencer = step_sequencer(mixer, bus)


#create events for activating either sample dock or step_sequencer
#find a way for another button press to send a sigint, and then clean up mixer

def play_step_sequencer(channel):
    """triggered by button press event"""
    #trigger lights and other haptics
    while True:
        stepSequencer.play_step_sequence()


def end_step_sequencer(channel):
    """kills step sequencer thread"""
    print("end loop")


def load_new_sound():
    """reads resistance value of node in loading dock, and assigns
    an audio file to that node, basedf on selection from potentiometer"""
    arduino_input = bus.read_i2c_block_data(0x03, 0, 2)#reading 2 bytes, first is resistor value, second is rotary encoder value
    resistor_value = arduino_input[0]
    rotary_encoding = arduino_input[1]
    mixer.reassign_sound(to_sound_code(resistor_value), rotary_encoding)

GPIO.add_event_detect(17, GPIO.RISING, callback=play_step_sequencer, bouncetime=250)
GPIO.add_event_detect(27, GPIO.RISING, callback=load_new_sound, bouncetime=250)



while True:
    time.sleep(0.1)

#play_step_sequencer()
