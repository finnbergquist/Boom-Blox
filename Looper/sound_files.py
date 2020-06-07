import pygame
from pygame import mixer

class mix:
    pygame.mixer.pre_init(22050, -16, 2, 256)#22050=default frequecy,-16=size(16 signed bits per audio sample
    pygame.mixer.init()                      #2-->stereo sound, 512=buffersize
    pygame.init()
    
    #initialize channels in the mixer
    channels = [pygame.mixer.Channel(0), pygame.mixer.Channel(1)]
    
    #sounds dictionary
    sounds = {
        "001" : pygame.mixer.Sound("Audio_Files/Track2.wav"),
        "010" : pygame.mixer.Sound("Audio_Files/drums.wav"),
        "100" : pygame.mixer.Sound("Audio_Files/Track3.wav"),
        "002" : pygame.mixer.Sound("Audio_Files/2_SECOND_PIANO.wav"),
        "020" : pygame.mixer.Sound("Audio_Files/Track1.wav")
    }

    def play(self, sound_code, channel_number):
        """Play arg1 sound in arg2 channel           
        ex) mix.play(1, 0) will play sound 1 in channel 0"""
        #make code readable by dict
        
        code = "'" + sound_code + "'"
        if (code in self.sounds):#there is no audio file in this position, so do nothing
            print("sound not in dictionary")
        else:#play specified sound in specified channel
            if sound_code == "000":#don't play any sound
                print("blank sound")
                return
            else:
                self.channels[channel_number].play(self.sounds[sound_code])#play that mf Sound!!
            
    
    def update_channel_volume(self, channel_number, volume):
        """sets the volume of a specific chanel"""     
        self.channels[channel_number].set_volume(volume)
        
        
    
    def cleanup(self):#need to use an exception handler!!!!! in driver
        """called at end of driver"""
        pygame.quit()