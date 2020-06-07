"""Audio Looper driver method"""
import time
# from gpiozero import MCP3008, PWMLED
from channel_structure import channels
from sound_files import mix
import time


"""The step_sequencer class holds all the information about the sequencer region of this device.
It contains a channel_structure object(AKA: channels), and the channel_structure can be manipulated, 
using the methods in that class(ex: ). This class also has a loop method, that plays the steps
from the channel_structure objects, using methods in the sounf_files class"""
class step_sequencer:

    def __init__(self, mixer):#mixer is global variable, so it can be accessed everywhere
        self.mixer = mixer
        self.channel_structure = channels(120, 2, 8)#2 channels, 8 steps
    

    def play_region(self, region_number):
        """helper method for step_sequencer_loop"""
        self.mixer.play(self.channel_structure.get_audio_num(0, region_number), 0)
        self.mixer.play(self.channel_structure.get_audio_num(1, region_number), 1)
        print(self.channel_structure.get_audio_num(0, region_number))
        print(self.channel_structure.get_audio_num(1, region_number))




    def step_sequencer_loop(self):
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
                    self.play_region(int(step/20))#plays audio files at steps 0,1,2,3,4,5,6,7
                # mixer.update_channel_volume(0, pot0.value)
                # mixer.update_channel_volume(1, pot1.value)
                next_time += 0.1





mixer = mix()
stepSequencer = step_sequencer(mixer)
stepSequencer.step_sequencer_loop()
