from symphony_sound_files import mix
from step_sequencer import step_sequencer
import RPi.GPIO as GPIO
import smbus2
import time

#setting up buttons
GPIO.setmode(GPIO.BCM)#normal gpio sumbering system
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

GPIO.add_event_detect(4, GPIO.RISING, callback=play_step_sequencer, bouncetime=250)


play_step_sequencer()
