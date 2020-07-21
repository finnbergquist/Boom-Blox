#ifndef Drum_channel_h
#define Drum_channel_h

#include "Arduino.h"
#include <bits/stdc++.h> 
using namespace std; 
#include <vector>

class Drum_channel {
    private:
        const char *inst_name;
        int max_steps;
        std::vector<int> steps;
        

    public:
        Drum_channel(const char *inst_name, int length);
        const char* getSound();
        int On(int index);
        void set(int index, int val);
};

#endif
