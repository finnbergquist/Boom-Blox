import pygame
from pygame import mixer

class mix:
    pygame.mixer.pre_init(22050, -16, 2, 256)#22050=default frequecy,-16=size(16 signed bits per audio sample
    pygame.mixer.init()                      #2-->stereo sound, 512=buffersize
    pygame.init()
    
    #initialize channels in the mixer
    channels = [pygame.mixer.Channel(0), pygame.mixer.Channel(1)]
    
    #implement dictionary with resistor values next!!!!!!
    sounds = [pygame.mixer.Sound("Audio_Files/Track1.wav"), pygame.mixer.Sound("Audio_Files/Track2.wav"), pygame.mixer.Sound("Audio_Files/drums.wav"),
              pygame.mixer.Sound("Audio_Files/Track3.wav"), pygame.mixer.Sound("Audio_Files/2_SECOND_PIANO.wav")]
    
    
    def play(self, sound_number, channel_number):
        """Play arg1 sound in arg2 channel           
        ex) mix.play(1, 0) will play sound 1 in channel 0"""
        
        if sound_number == 0:#there is no audio file in this position, so do nothing
            return
        else:#play specified sound in specified channel
            self.channels[channel_number].play(self.sounds[sound_number - 1])
            
    
    
    def update_channel_volume(self, channel_number, volume):
        """sets the volume of a specific chanel"""     
        self.channels[channel_number].set_volume(volume)
        
        
    
    def cleanup(self):#need to use an exception handler!!!!! in driver
        """called at end of driver"""
        pygame.quit()