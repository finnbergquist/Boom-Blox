#include "Sequencer.h"
#include "Clock.h"
#include "Drum_channel.h"
#include <Audio.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SerialFlash.h>

// GUItool: begin automatically generated code
AudioPlaySdWav           playSdWav1;     //xy=165,133
AudioPlaySdWav           playSdWav2;     //xy=167,364
AudioMixer4              mixer1;         //xy=385,251
AudioMixer4              mixer2;         //xy=388,362
AudioOutputI2S           i2s1;           //xy=777,309
AudioConnection          patchCord1(playSdWav1, 0, mixer1, 0);
AudioConnection          patchCord2(playSdWav1, 1, mixer2, 0);
AudioConnection          patchCord3(playSdWav2, 0, mixer1, 1);
AudioConnection          patchCord4(playSdWav2, 1, mixer2, 1);
AudioConnection          patchCord5(mixer1, 0, i2s1, 0);
AudioConnection          patchCord6(mixer2, 0, i2s1, 1);
AudioControlSGTL5000     sgtl5000_1;     //xy=394.00000762939453,228.00003051757812

#define SDCARD_CS_PIN    10
#define SDCARD_MOSI_PIN  7
#define SDCARD_SCK_PIN   14

Sequencer sequence(5,4);
Clock new_clock(112,16);
//const char *inst = "KICK.WAV";
Drum_channel kick("KICK.WAV", 16);
//Drum_channel snare("SNARE.WAV", 16);
//
//Drum_channel trial("TRIAL.WAV", 16);

void setup(){
    Serial.begin(9600);   
    AudioMemory(15);
    sgtl5000_1.enable();
    sgtl5000_1.volume(0.5);
    
    SPI.setMOSI(SDCARD_MOSI_PIN);
    SPI.setSCK(SDCARD_SCK_PIN);
    if (!(SD.begin(SDCARD_CS_PIN))) {
      while (1) {
        Serial.println("Unable to access the SD card");
        delay(500);
      }
    }
    
    new_clock.start_clock();
//    trial.set(1, 1);
//    snare.set(3, 1);
//    snare.set(7, 1);   
//    snare.set(11, 1);      
//    snare.set(15, 1);

    kick.set(1, 1);
    kick.set(4, 1);
    kick.set(9, 1);
    kick.set(10, 1);
    kick.set(12, 1);
    kick.set(14, 1);
//    playSdWav1.play(trial.getSound());
    
}

void loop() { 
    if (new_clock.change() == true) {
      
//      if (snare.On(new_clock.getStep()) == 1) {      
//        playSdWav2.play(snare.getSound());
//        
//      }
      if (kick.On(new_clock.getStep()) == 1) {      
        playSdWav1.play(kick.getSound());
        
      }
    }

}
