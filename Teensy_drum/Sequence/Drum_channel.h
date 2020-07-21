#ifndef Drum_channel_h
#define Drum_channel_h

#include "Arduino.h"

class Drum_channel {
    private:
        const char *inst_name;
        int max_steps;
        int steps [32];
        

    public:
        Drum_channel(const char *inst_name, int length);
        const char* getSound();
        int On(int index);
        void set(int index, int val);
};

#endif
