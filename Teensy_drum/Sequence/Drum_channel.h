#include <Audio.h>
#include <SD.h>
#include "Arduino.h"

#ifndef Drum_channel_h
#define Drum_channel_h



class Drum_channel {
    private:
        const char *inst_name;
        int max_steps;
        int steps [32];
        AudioPlaySdWav instr;
        

    public:
        Drum_channel(const char *inst_name, int max_steps, AudioPlaySdWav instr);
        const char* getSound();
        int On(int index);
        void Trigger();
        void set(int index, int val);
        AudioPlaySdWav get_instr();
};

#endif
