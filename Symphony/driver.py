from symphony_sound_files import mix
from step_sequencer import step_sequencer
import RPi.GPIO as GPIO
import smbus2
import time
import os
import signal

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

def play_step_sequencer():
    """triggered by button press event"""
    #trigger lights and other haptics
    stepSequencer.step_sequencer_loop()

def end_step_sequencer():
    """kills step sequencer thread"""
    os.kill(p.pid,signal.SIGINT)

def signal_handler(frame):
    mixer.cleanup()
    print("mixer cleaned up")


def load_new_sound():
    """reads resistance value of node in loading dock, and assigns
    an audio file to that node, basedf on selection from potentiometer"""

GPIO.add_event_detect(17, GPIO.RISING, callback=play_step_sequencer, bouncetime=250)
GPIO.add_event_detect(27, GPIO.RISING, callback=end_step_sequencer, bouncetime=250)
signal.signal(signal.SIGINT, signal_handler)


#play_step_sequencer()
