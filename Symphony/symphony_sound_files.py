import pygame
from pygame import mixer
from gpiozero import MCP3008


class mix:
    pygame.mixer.pre_init(22050, -16, 2, 256)#22050=default frequecy,-16=size(16 signed bits per audio sample
    pygame.mixer.init()                      #2-->stereo sound, 512=buffersize
    pygame.init()
    #set volume 
    #pygame.mixer.music.set_volume(1.0)
    
    #initialize channels in the mixer
    channels = [pygame.mixer.Channel(0), pygame.mixer.Channel(1),
                pygame.mixer.Channel(2), pygame.mixer.Channel(3)]

    pots = [MCP3008(0), MCP3008(1), MCP3008(2), MCP3008(3)]

    
    #sounds dictionary
    # Accessing sounds:  
#     these codes that will inform the Raspi which .wav to play.

#       First digit is length, then sound (change!), then effect.

    
    sound_files = [pygame.mixer.Sound("Audio_Files/2barschimes.wav"),
                   pygame.mixer.Sound("Audio_Files/2barscrash.wav"),
                   pygame.mixer.Sound("Audio_Files/4barsguitar.wav"),
                   pygame.mixer.Sound("Audio_Files/4barspiano.wav"),
                   pygame.mixer.Sound("Audio_Files/8barsharp.wav")]
    
    sound_assignments = {
        "200" : sound_files[0],
        "210" : sound_files[1],
        "400" : sound_files[2],
        "410" : sound_files[3],
        "800" : sound_files[4]        
    }


    #this play method should used in the step sequencer
    def play_step(self, sound_code, channel_number): 
            """Play sound at certain step in specified channel"""           
            if sound_code == '000':
                return
            else:#play specified sound in specified channel
                # print(type(code))
                # print(self.sounds.get(code))
                self.channels[channel_number].play(self.sound_assignments[sound_code])            


    def update_channel_volume(self):
        """sets the volume of a all chanells to values of pots"""  
        for i in range(0,4):
            self.channels[i].set_volume(self.pots[i].value)
            
    def reassign_sound(self, sound_code, sound_number):
        """reassigning process done in the sample loading dock"""
        self.sound_assignments.update({sound_code: sound_files[sound_number]})
            
    def cleanup(self):#need to use an exception handler!!!!! in driver
        """called at end of driver"""
        pygame.quit()